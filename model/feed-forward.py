import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data import Dataset, DataLoader

import text2emotion as te

class ScoreDataset(Dataset):

    def __init__(self, text_path, label_path=None):
        self.all_scores = []
        text_file = open(text_path, "r")
        for scores in text_file:
            all_scores.append(scores)
        self.labels = []
        if label_path is not None:
            label_file = open(label_path, "r")
            for label in label_file:
                self.labels.append[label]

    def __len__(self):
        return len(self.all_scores)

    def __getitem__(self, i):
        scores = self.all_scores[i]
        emotion = te.get_emotion(scores[-1])
        scores = scores[:-1]
        scores = [float(s) for s in scores]
        scores.append(emotion['Angry'])
        scores.append(emotion['Fear'])
        scores.append(emotion['Happy'])
        scores.append(emotion['Sad'])
        scores.append(emotion['Surprise'])

        if len(self.labels) == 0:
                        
        

class Model(nn.Module):

    def __init__(self):

    def forward(self, x):

if (len(sys.argv)) != 3:
    print("Please provide --train or --test and file to open")
mode = sys.argv[1]
filename = sys.argv[2]

if mode == "--train":
    model = Model()
    
    data_loader = DataLoader

if mode == "--test":
