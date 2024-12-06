file = open("day5.txt", "r")
rules = file.read()
rules = rules.split("\n")

organise = False
ruleList = []
total = 0

for r in rules:
    if r == "":
        organise = True
        continue

    if not organise:
        rule = r.split("|")
        if rule[1] in ruleList and rule[0] not in ruleList:
            ruleList.insert(ruleList.index(rule[1]), rule[0])
        elif rule[1] not in ruleList and rule[0] not in ruleList:
            ruleList.insert(-1, rule[0])
            ruleList.insert(-1, rule[1])
        elif rule[1] not in ruleList and rule[0] in ruleList:
            ruleList.insert(ruleList.index(rule[0]) + 1, rule[1])
        else:
            if ruleList.index(rule[0]) > ruleList.index(rule[1]):
                ruleList.remove(rule[0])
                ruleList.insert(ruleList.index(rule[1]), rule[0])
    else:
        pageOrder = []
        order = r.split(",")
        for rule in ruleList:
            if rule in order:
                pageOrder.append(rule)
        print(pageOrder, order)
        if pageOrder == order:
            total += int(pageOrder[int(len(pageOrder) / 2)])
            print("m =", pageOrder[int(len(pageOrder) / 2)], "from", pageOrder)

print(ruleList)
print(total)