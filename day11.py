stones = list(map(int, input().split()))

resultPairs = {}
def stoneMul(stone, count, endLimit):
    length = len(str(stone))
    if count==endLimit:
        return 1
    if (stone, count) in resultPairs:
        return resultPairs[(stone, count)]
    sum = 0
    if stone == 0 :
        sum =  stoneMul(1, count+1, endLimit)
    elif length%2==0:
        sum += stoneMul(stone//(10**(length//2)), count+1, endLimit)
        sum += stoneMul(stone%(10**(length//2)), count+1, endLimit)
    else:
        sum = stoneMul(stone*2024, count+1, endLimit)
    if stone not in resultPairs:
        resultPairs[(stone, count)] = sum
    return sum


count = 0
for i in range(len(stones)):
    count += stoneMul(stones[i], 0, 25)
print("Answer part 1: ", count)
count2 = 0
resultPairs = {}
for i in range(len(stones)):
    count2 += stoneMul(stones[i], 0, 75)
print("Answer part 2: ", count2)


