file = open("day1.txt", "r")
locIn = file.read()

left = []
right = []

total = 0
simScore = 0

locIn = locIn.split("\n")

for line in locIn:
    line = line.split("   ")
    left.append(line[0])
    right.append(line[1])

left.sort()
right.sort()

for i in range(len(left)):
    simScore += int(left[i]) * right.count(left[i])
    total += abs(int(left[i]) - int(right[i]))

print("Total:", total)
print("Sim score:", simScore)