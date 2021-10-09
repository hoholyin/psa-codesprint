from random import randrange
import text2emotion as te

emotions_file = open("emotions.txt", "r")
emotions = [e[:-1] for e in emotions_file]
x_train = open("x_test.txt", "w")
y_train = open("y_test.txt", "w")
    
for i in range(200):
    scores = ""
    rating = 0
    positive = True
    for j in range(10):
        if (i % 3 == 0):
            val = randrange(2)
        elif (i % 4 == 0):
            val = randrange(1, 3)
        elif (i % 7 == 0):
            val = randrange(4, 5)
        else:
            val = randrange(3, 5)
        rating += (val + 1) * 0.2
        scores += str(val) + " "
    if rating >= 6:
        positive = False
    for j in range(3):
        done = False
        while not done:
            emotion = emotions[randrange(len(emotions))]
            em_object = te.get_emotion(emotion)
            score1 = em_object['Angry']
            score2 = em_object['Fear']
            score4 = em_object['Sad']
            avg_score = (score1 + score2 + score4) / 3
            if positive and score1 + score2 + score4 < 0.3:
                done = True
            elif not positive and score1 + score2 + score4 > 0.7:
                done = True
        rating += avg_score
        scores += emotion + " "

    x_train.write(scores[:-1] + "\n")
    avg_y = rating / 13
    y_train.write(str(avg_y) + "\n")
    
