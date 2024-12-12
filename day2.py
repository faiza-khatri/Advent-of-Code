def safeReport(rep):
    diff = rep[1] - rep[0]
    inc = (diff >= 0)
    safeRep = False
    if abs(diff) >= 1 and abs(diff) <= 3:
        safeRep = True
        for j in range(2, len(rep)):
            diff = rep[j] - rep[j-1]
            if inc != (diff >= 0) or abs(diff) < 1 or abs(diff) > 3:
                safeRep = False
                break
    return safeRep

safeCount = 0
safeCount1= 0
for i in range(1000):
    report = list(map(int, input().split()))
    safe = False
    if safeReport(report):
        safeCount1+=1
        safe = True
    else:
        for k in range(len(report)):
            if safeReport(report[:k] + report[k+1:]):
                safe = True
    if safe:
        safeCount+=1

print("Answer part 1: ", safeCount1)
print("Answer part 2: ", safeCount)

