from random import randrange

names = open("names.txt", "r")
result_file = open("responses.txt", "w")
for name in names:
    responses = name[:-2]
    for i in range(10):
        responses += str(randrange(5)) + " "
    result = responses[:-1] + "\n"
    result_file.write(result)

