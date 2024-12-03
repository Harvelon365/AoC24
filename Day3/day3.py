file = open("day3.txt", "r")
instructions = file.read()
instructions = instructions.split("\n")

total = 0
execute = True

for line in instructions:
    print(line)
    line = line.split("mul(")
    for section in line:
        print(execute, "-", section)
        if not execute:
            if "do()" in section:
                execute = True
            continue
        if "don't()" in section:
            execute = False
        first = ""
        second = ""
        moveToSecond = False
        for char in section:
            if char == ',' and first != "":
                moveToSecond = True
                continue
            if char == ')' and moveToSecond:
                total += int(first) * int(second)
                break
            if not char.isnumeric():
                break

            if not moveToSecond:
                first += char
            else:
                second += char

print(total)