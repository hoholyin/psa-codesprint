from random import randrange
import json

names = open("names.txt", "r")
result_file = open("employee_data.txt", "w")
for name in names:
    name = name[:-2]

    #Add number
    number = "9"
    for i in range(7):
        number += str(randrange(10))

    #Add email
    email = name[:-1].lower().replace(" ", "") + "@globalpsa.com"

    #Add dept
    dept = "NGTPSD"
    
    result = {
        'name': name,
        'contact': number,
        'email': email,
        'department': dept 
    } 
    result_file.write(json.dumps(result) + "\n")
