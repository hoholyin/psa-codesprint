from random import randrange
import requests
import json
import text2emotion as te

names = open("names.txt", "r")
emotions = open("emotions.txt", "r")
emotions = [e[:-1] for e in emotions]
i = 0
for name in names:
    scores = []
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
        scores.append(str(val))
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
        scores.append(emotion)

    payload = {
        'name': name[:-3],
        'scores': scores
    }
    print(payload)
    r = requests.post('https://codesprint.brandoncjh.repl.co/submitscore', json=payload)
    print("submitted entry for {}".format(name))
    i += 1

