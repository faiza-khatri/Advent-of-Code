# yet to make input lines dynamic
lst1 = []
lst2 = []
for i in range(1000):
    x, y = list(map(int, (input().split())))
    lst1.append(x)
    lst2.append(y)

simScore = 0
for i in range(len(lst1)):
    simScore += (lst1[i]*lst2.count(lst1[i]))

lst1.sort()
lst2.sort()
differenceSum = 0
for i in range(len(lst1)):
    differenceSum += abs(lst1[i] - lst2[i])
print("Answer part 1: ", differenceSum)
print("Answer part 2: ", simScore)