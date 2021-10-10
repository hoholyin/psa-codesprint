import requests
import sys

names = open("names.txt", "r")
names = [n[:-3] for n in names]

prediction = open("prediction.txt", "r")
prediction = [p for p in prediction]

if (len(names) != len(prediction)):
    sys.exit()

for i in range(len(names)):
    payload = {
        'name': names[i],
        'rating': str(1 - float(prediction[i]))
    }
    r = requests.post('https://codesprint.brandoncjh.repl.co/submitrating', json=payload)
    print("submitted rating for {}".format(names[i]))

