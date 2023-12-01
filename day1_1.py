caldoc = []
with open('day1input.txt', 'r') as sourcefile:
    for line in sourcefile:
        caldoc.append(line.strip())

#testlist = ["cs4gtegfce5ve", "1csfffenz34unnu3", "fcvneen2nje3", "12"]

sum = 0

for element in caldoc:
    l = []
    for char in element:
        try:
            int(char)
            l.append(char)
        except:
            continue
    calnumb = int(l[0]+l[len(l)-1])
    sum += calnumb

print(sum)