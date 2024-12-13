# file = 'testInput.txt'
file = 'inputDay13.txt'

def extract(line, char):
    parts = [el.split(',') for el in line.split(char)[-2:]]
    return int(parts[0][0]), int(parts[1][0])

def calculate(xa, ya, xb, yb, x, y):
    eqx = (ya*xa, ya*xb, ya*x)
    eqy = (xa*ya, xa*yb, xa*y)

    b = (eqx[2]-eqy[2])/(eqx[1]-eqy[1])
    a = (eqx[2]-(eqx[1]*b))/eqx[0]

    return a, b

with open(file, 'r') as file:
    content = file.read()

sections = content.strip().split('\n\n')
total = 0
total2 = 0
for section in sections:
    a, b, loc = section.strip().split('\n')
    xa, ya = extract(a, "+")
    xb, yb = extract(b, "+")
    x, y = extract(loc, "=")

    a, b = calculate(xa, ya, xb, yb, x, y)

    if a <=100 and b <= 100 and int(a)-a == 0 and int(b)-b==0:
        total += ((a*3)+b)

    aMod, bMod = calculate(xa, ya, xb, yb, x+10000000000000, y+10000000000000)

    if int(aMod)-aMod == 0 and int(bMod)-bMod == 0:
        total2 += ((aMod*3)+bMod)

print("Answer 1: ", total)
print("Answer 2: ", total2)
    