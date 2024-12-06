file = open("day4.txt", "r")
wordsearch = file.read()

wordsearch = wordsearch.split("\n")

total = 0

for i in range(len(wordsearch)):
    for j in range(len(wordsearch[i])):
        if wordsearch[i][j] == "X":
            for y in range(-1, 2, 1):
                for x in range(-1, 2, 1):
                    try:
                        if wordsearch[i+y][j+x] == "M" and wordsearch[i+y+y][j+x+x] == "A" and wordsearch[i+y+y+y][j+x+x+x] == "S":
                            total += 1
                            print(wordsearch[i][j], wordsearch[i+y][j+x], wordsearch[i+y+y][j+x+x], wordsearch[i+y+y+y][j+x+x+x])
                    finally:
                        continue

print(total)