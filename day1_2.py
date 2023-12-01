numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

caldoc = []
with open('day1input.txt', 'r') as sourcefile:
    for line in sourcefile:
        caldoc.append(line.strip())

#testlist = ["three4gtegfce5ve", "1csfffenz34unnu3two", "fcvnineneen2nje3", "12"]

sum = 0

for element in caldoc:
    l = []
    for char in range(len(element)):
        try:
            int(element[char])
            l.append(element[char])
        except:
            for number in range(len(numbers)):
                if len(numbers[number]) <= len(element)-char:
                    if numbers[number] == element[char:char+len(numbers[number])]:
                        l.append(str(number+1))
            
    calnumb = int(l[0]+l[len(l)-1])
    sum += calnumb

print(sum)