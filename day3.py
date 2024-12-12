
import re

def mul(x, y):
    return x*y

def getStrSum(string):
    sum = 0
    x = re.findall(r"mul\( *\d{1,3}, *\d{1,3} *\)", string)
    for el in x:
        sum += eval(el)
    return sum

sum = 0
line = ""
for i in range(6):
    line += input()

sum += getStrSum(line)
pattern = r"mul\( *\d{1,3}, *\d{1,3} *\)|don\'t\(\)|do\(\)"
matches = re.findall(pattern, line)

enabled = True
sum2 = 0
for i in range(len(matches)):
    if matches[i] == "don't()":
        enabled = False
    elif matches[i] == "do()":
        enabled = True
    elif enabled:
        sum2 += eval(matches[i])

print("Answer 1 : ", sum)
print("Answer 2 : ", sum2)

