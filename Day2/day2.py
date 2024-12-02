file = open("day2.txt", "r")
reports = file.read()
reports = reports.split("\n")

safecount = 0

for r in reports:
    r = r.split(" ")
    prev = -1
    direc = 0
    safe = True
    for i in range(len(r)):
        level = r[i]
        if prev == -1:
            prev = int(level)
            continue
        if int(level) == prev:
            safe = False
            break
        if direc == 0:
            if prev > int(level):
                direc = -1
            else:
                direc = 1
        if abs(int(level)-prev) > 3:
            safe = False
            break
        if direc == -1 and int(level) > prev:
            safe = False
            break
        if direc == 1 and int(level) < prev:
            safe = False
            break
        prev = int(level)

    if safe:
        safecount += 1
    else:
        safe = []
        for i in range(len(r)):
            tempR = r.copy()
            del tempR[i]
            direc = 0
            prev = -1
            tempSafe = True
            for j in range(len(tempR)):
                level = tempR[j]
                if prev == -1:
                    prev = int(level)
                    continue
                if int(level) == prev:
                    tempSafe = False
                    break
                if direc == 0:
                    if prev > int(level):
                        direc = -1
                    else:
                        direc = 1
                if abs(int(level) - prev) > 3:
                    tempSafe = False
                    break
                if direc == -1 and int(level) > prev:
                    tempSafe = False
                    break
                if direc == 1 and int(level) < prev:
                    tempSafe = False
                    break
                prev = int(level)
            safe.append(tempSafe)
        if True in safe:
            safecount += 1

print(safecount)