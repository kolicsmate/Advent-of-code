games = []
with open('day2input.txt', 'r') as sourcefile:
    i=0
    for line in sourcefile:
        a = line.strip().split(";")
        for i in range(len(a)):
            a[i] = a[i].split(",")
            for j in range(len(a[i])):
                a[i][j] = a[i][j].split(" ")
                del a[i][j][0]
                #a[i][0][0] = a[i][0][0][:1]
        del a[0][0][0]
        games.append(a)

sum = 0

for game in games:
    fewest = [0,0,0]
    for reveal in game:
        for color in reveal:
            if color[1]== "red" and int(color[0]) > fewest[0]:
                fewest[0] = int(color[0])
            elif color[1]== "green" and int(color[0]) > fewest[1]:
                fewest[1] = int(color[0])
            elif color[1]== "blue" and int(color[0]) > fewest[2]:
                fewest[2] = int(color[0])
    sum += fewest[0]*fewest[1]*fewest[2]

print(sum)