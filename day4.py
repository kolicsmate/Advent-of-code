file = open("day4input.txt", "r")

summa = 0

scrcards = []
for line in file:
    scrcards.append(line)
cards = []

for i in range(len(scrcards)):
    cards.append(1)

print(cards)
i = 0

for line in scrcards:
    line = line.split(":")[1]

    a = line.split("|")[0]
    b = line.split("|")[1]

    a = a.split()
    b = b.split()

    print(set(a), set(b))
    n = len(set(a) & set(b))

    if n > 0:
        summa += 2**(n-1)

    for j in range(n):
        cards[i + j + 1] += cards[i]

    i += 1

print(summa, sum(cards))