import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

import text2emotion as te

class ScoreDataset(Dataset):

    def __init__(self, text_path, label_path=None):
        self.all_scores = []
        text_file = open(text_path, "r")
        for scores in text_file:
            self.all_scores.append(scores)
        self.labels = []
        if label_path is not None:
            label_file = open(label_path, "r")
            for label in label_file:
                self.labels.append(label.rstrip())

    def __len__(self):
        return len(self.all_scores)

    def __getitem__(self, i):
        scores = self.all_scores[i]
        emotion = te.get_emotion(scores[-1])
        scores = scores[:-1].split(" ")
        for j in range(3):
            idx = -(j + 1)
            emotion_obj = te.get_emotion(scores[idx])
            score = (emotion_obj['Angry'] + emotion_obj['Sad'] + emotion_obj['Fear']) / 3
            scores[idx] = score
        scores = [float(s) for s in scores]
        scores_tensor = torch.FloatTensor(scores)

        labels = [0.2, 0.4, 0.6, 0.8, 1]
        if len(self.labels) == 0:
            return scores_tensor, torch.zeros(5) 
        label = float(self.labels[i])
        if (label <= 0.2):
            label = 0.2
        elif label <= 0.4:
            label = 0.4
        elif label <= 0.6:
            label = 0.6
        elif label <= 0.8:
            label = 0.8
        else:
            label = 1
        def check_label_same(sample, actual):
            return 1 if sample == actual else 0
        label_tensor = torch.LongTensor([check_label_same(l, label) for l in labels])
        return scores_tensor, label_tensor
        

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        hidden_dim = 100
        self.ffl_1 = nn.Linear(13, hidden_dim)
        self.out = nn.Linear(hidden_dim, 5)

    def forward(self, x):
        v = self.ffl_1(x)
        v = self.out(v)
        return v

if (len(sys.argv)) != 4:
    print("Please provide --train or --test and file to open")
    exit()
mode = sys.argv[1]
x_train = sys.argv[2]
y_train = sys.argv[3]
device = 'cpu'

if mode == "--train":
    dataset = ScoreDataset(x_train, y_train) 
    model = Model()
    learning_rate = 0.01
    batch_size = 4
    num_epochs = 20
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    def get_index(target_list):
        return target_list.index(max(target_list))
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for step, data in enumerate(data_loader, 0):
            
            scores = data[0].to(device)
            labels = data[1].to(device)

            labels = torch.LongTensor([get_index(l) for l in labels.tolist()])

            optimizer.zero_grad()

            outputs = model(scores)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

            if (step % 100 == 99):
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, step + 1, running_loss / 100))
                running_loss = 0.0

    checkpoint = {
        'model': model
    }
    torch.save(checkpoint, 'model.pt')
    print("Model saved in model.pt")
        

if mode == "--test":
    checkpoint = torch.load('model.pt')
    model = checkpoint['model']
    dataset = ScoreDataset(x_train) # they are testing data
    model.eval()
    data_loader = DataLoader(dataset, batch_size=20, shuffle=False)
    class_map = [0.2, 0.4, 0.6, 0.8, 1]
    labels = []
    with torch.no_grad():
        for data in data_loader:
            scores = data[0].to(device)
            outputs = model(scores).cpu()
            info, batch_label = torch.max(outputs.data, 1)
            batch_label = [class_map[x] for x in batch_label.tolist()]
            labels.extend(batch_label)
    prediction = open("prediction.txt", "w")
    for label in labels:
        prediction.write(str(label) + "\n")
    correct = 0
    '''
    answers = open(y_train, "r")
    answers = [a for a in answers]
    if len(answers) != len(labels):
        print("length of prediction does not match")
        exit()
    for i in range(len(labels)):
        mark = 1 if float(answers[i]) < float(labels[i]) and float(answers[i]) > float(labels[i]) - 0.2 else 0
        correct += mark
    acc = float(correct) / float(len(answers))
    print("Accuracy is ", acc)
    '''
