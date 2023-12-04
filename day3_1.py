engsche = []
with open('day3input.txt', 'r') as sourcefile:
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



g = []

for number in numbers:
    numberfield = []
    
    i = -1
    while i < number[2]+1:
        numberfield.append(engsche[number[0]-1][number[1]+i])
        numberfield.append(engsche[number[0]+1][number[1]+i])
        i += 1
                   
    numberfield.append(engsche[number[0]][number[1]-1])
    numberfield.append(engsche[number[0]][number[1]+number[2]])
            
    g.append(numberfield)

partnumber = []

for fd in range(len(g)):
    k = 0
    for d in g[fd]:
        if d != "." or type(d) == int:
            k += 1
    if k > 0:
        partnumber.append(fd)

sum = 0

for i in partnumber:
    x = engsche[numbers[i][0]]
    y = int(x[numbers[i][1]:numbers[i][1]+numbers[i][2]])
    sum += y

print(sum)

print(numbers)