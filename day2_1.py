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
bagcon = (12,13,14)
var = 1
for game in games:
    check = 0
    for reveal in game:
        suml = [0,0,0]
        for color in reveal:
            if color[1]== "red":
                suml[0] += int(color[0])
            elif color[1]== "green":
                suml[1] += int(color[0])
            elif color[1]== "blue":
                suml[2] += int(color[0])
        if suml[0] <= bagcon[0] and suml[1] <= bagcon[1] and suml[2] <= bagcon[2]:
            check+=1
    if check == len(game):
        sum += var
    var += 1

print(sum)