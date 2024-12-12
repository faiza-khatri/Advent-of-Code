nTest = 1176
# nTest = 21
rules = {}
for i in range(nTest):
    x, y = list(map(int, input().split("|")))
    if x in rules:
        rules[x].append(y)
    else:
        rules[x] = [y]

input()
tests = 209
# tests = 6
sum = 0
sum1 = 0
for i in range(tests):
    report = list(map(int, input().split(",")))

    isSafe = True
    for j in range(1, len(report)):
        if report[j] in rules:

            for k in range(j):
                if report[k] in rules[report[j]]:
                    isSafe = False
    if isSafe:
        if len(report)%2==0:
            sum1 += report[len(report)//2]
        else:
            sum1 += report[len(report)//2]
    ordered = []
    if not isSafe:

        ordered.append(report[0])
        for j in range(1, len(report)):
            insertIdx = j
            if report[j] in rules:

                for k in range(len(ordered)-1, -1, -1):
                    if ordered[k] in rules[report[j]]:
                        insertIdx = k
                    
            ordered.insert(insertIdx, report[j])


        sum += ordered[len(ordered)//2]

print("Answer 1: ", sum1)
print("Answer 2: ", sum)
