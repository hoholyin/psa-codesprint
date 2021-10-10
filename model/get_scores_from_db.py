import requests

names = open("names.txt", "r")
scores = open("scores.txt", "w")
names = [n[:-3] for n in names]
for name in names:
    payload = { 'name': name } 
    url = 'https://codesprint.brandoncjh.repl.co/getscorebyname'
    r = requests.get(url, params=payload)
    scores.write(" ".join(r.json()['employeeScore']) + "\n")
