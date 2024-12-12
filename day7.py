# def canReachTarget(target, numbers, idx = 0, current=0):
#     if target == current and idx == len(numbers):
#         return True
#     if idx == len(numbers) or current > target:
#         return False
#     if canReachTarget(target, numbers, idx+1, current + numbers[idx]):
#         return True
#     if current != 0 and canReachTarget(target, numbers, idx + 1, current * numbers[idx]):
#         return True
#     if canReachTarget(target, numbers, idx+1, int(str(current)+str(numbers[idx]))):
#         return True


# used the above function for calculation and submission, and then optimised the code below later
def canReachTargetBackTrack(numbers, idx, current):
    if idx == 0 and current == numbers[0]:
        return True
    if idx == 0 or current <= 0:
        return False
    if canReachTargetBackTrack(numbers, idx-1, current - numbers[idx]):
            return True
    if current % numbers[idx] == 0 and canReachTargetBackTrack(numbers, idx-1, current // numbers[idx]):
        return True
    numStr = str(numbers[idx])
    currentEnd = current % (10**len(numStr))
    current = current // (10**len(numStr))
    if currentEnd==numbers[idx] and canReachTargetBackTrack(numbers, idx -1, current):
        return True
    
def canReachTargetBackTrack1(numbers, idx, current):
    if idx == 0 and current == numbers[0]:
        return True
    if idx == 0 or current <= 0:
        return False
    if canReachTargetBackTrack1(numbers, idx-1, current - numbers[idx]):
            return True
    if current % numbers[idx] == 0 and canReachTargetBackTrack1(numbers, idx-1, current // numbers[idx]):
        return True
    
    
   
    
# nLines = 9
import time
start = time.time()
nLines = 850
count = 0
count1 = 0
for _ in range(nLines):
    lst = input().split(": ")
    num = int(lst[0])
    numbers = list(map(int, lst[1].split()))
    if canReachTargetBackTrack(numbers, len(numbers)-1, num):
        count += num
    if canReachTargetBackTrack1(numbers, len(numbers)-1, num):
        count1 += num
print("Answer 1: ", count1)
print("Answer 2: ", count)
stop = time.time()
print(f"Execution time: {stop-start:4.1f} s")
    
