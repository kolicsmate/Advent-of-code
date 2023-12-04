engsche = []
with open('day3testinput.txt', 'r') as sourcefile:
    for line in sourcefile:
        engsche.append(line.strip())

for i in range(len(engsche)):
    engsche[i] = "." + engsche[i] + "."

engsche.insert(0, "." *(len(engsche[0])+2))
engsche.append("."*(len(engsche[0])+2))

numbers = []

for line in range(len(engsche)):
    char = 0
    while char < len(engsche[line]):
        try:
            int(engsche[line][char])
            inte = True
            lenght = 1
            while inte:
                try:
                    int(engsche[line][char+lenght])
                    lenght += 1
                except:
                    inte = False
            a = [line, char, lenght]
            numbers.append(a)
            char += lenght
        except:
            char += 1

stars = []
for number in numbers:
    i = -1
    while i < number[2]+1:
        a = engsche[number[0]-1][number[1]+i]
        b = engsche[number[0]+1][number[1]+i]

        if a == "*":
            cor = [number[0]-1, number[1]+i]
            stars.append(cor)
        if b == "*":
            cor = [number[0]+1, number[1]+i]
            stars.append(cor)

        i += 1

    c = engsche[number[0]][number[1]-1]
    d = engsche[number[0]][number[1]+number[2]]

    if c == "*":
        cor = [number[0], number[1]-1]
        stars.append(cor)
    if d == "*":
        cor = [number[0], number[1]+number[2]]
        stars.append(cor)


stars2= []
for item in stars:
    if item not in stars2:
        stars2.append(item)

numnextstars = []
for e in stars2:
    i = -1
    asd = []
    while i < 2:
        try:
            int(engsche[e[0]-1][e[1]+i])
            if len(asd) < 2:
                asd.append([e[0]-1,e[1]+i])
        except:
            next
        try:
            int(engsche[e[0]+1][e[1]+i])
            if len(asd) < 2:
                asd.append([e[0]+1,e[1]+i])
        except:
            next
        i += 1

    try:
        int(engsche[e[0]][e[1]-1])
        if len(asd) < 2:
            asd.append([e[0],e[1]-1])
    except:
        next
    try:
        int(engsche[e[0]][e[1]+1])
        if len(asd) < 2:
            asd.append([e[0],e[1]+1])
    except:
        next
    
    numnextstars.append(asd)


print()
newnum = []
for e in numbers:
    fal = []
    for i in range(e[2]):
        fal.append([e[0],e[1]+i])
    newnum.append(fal)


cékla = []
for w in range(len(numnextstars)):
    z = []
    if len(numnextstars[w]) == 2:
        for x in range(2):
            for i in newnum:
                for j in i:                    
                    if j == numnextstars[w][x]:
                        z.append(i)
    if z != []:
        cékla.append(z)
             

sum = 0

for i in cékla:
    cd = 1
    for k in i:
        kl = ''
        for j in k:
            kl += engsche[j[0]][j[1]]
        cd *= int(kl)
    sum += cd

print(sum)


print(cékla)
print(newnum)
print(numbers)
print(numnextstars)