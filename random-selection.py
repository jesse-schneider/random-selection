import random

line_count = 0
data = []

with open("data.txt", "r") as file:
    line = file.readline()
    data.append(line.strip())
    line_count += 1

    while line:
        print("Line {}: {}".format(line_count, line.strip()))
        line = file.readline()
        if line != '':
            data.append(line.strip())
            line_count += 1


for i in range(len(data)):
    print(data[i])

print("\nrandom.choice() has been used to select iPad winner\n")
print("The winner is ..... ", random.choice(data))

file.close()