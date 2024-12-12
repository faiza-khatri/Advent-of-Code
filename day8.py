nLines = 50
# nLines = 12
graph = {}
for i in range(nLines):
    row = input().strip()
    for j in range(len(row)):
        if row[j] != ".":
            graph.setdefault(row[j], []).append((i, j))
rows, cols = i, j

def part1():
    uniquePos = set()
    for k, v in graph.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                difference = (v[j][0]-v[i][0], v[j][1]-v[i][1])
                firstPos = (v[i][0]-difference[0], v[i][1]-difference[1])
                secondPos = (v[j][0]+difference[0], v[j][1]+difference[1])
                if 0 <= firstPos[0] <= rows and 0 <= firstPos[1] <= cols: 
                    uniquePos.add(firstPos) 
                if 0 <= secondPos[0] <= rows and 0 <= secondPos[1] <= cols: 
                    uniquePos.add(secondPos)
    return len(uniquePos)

def part2():
    uniquePos = set()

    for k, v in graph.items():
        for i in range(len(v)):
            uniquePos.add(v[i])
            for j in range(i+1, len(v)):
                uniquePos.add(v[j])
                difference = (v[j][0]-v[i][0], v[j][1]-v[i][1])
                firstPos = (v[i][0]-difference[0], v[i][1]-difference[1])
                secondPos = (v[j][0]+difference[0], v[j][1]+difference[1])
                while 0 <= firstPos[0] <= rows and 0 <= firstPos[1] <= cols: 
                    uniquePos.add(firstPos) 
                    firstPos = (firstPos[0]-difference[0], firstPos[1] - difference[1])
                while 0 <= secondPos[0] <= rows and 0 <= secondPos[1] <= cols: 
                    uniquePos.add(secondPos)
                    secondPos = (secondPos[0] + difference[0], secondPos[1] + difference[1])
    return len(uniquePos)

print("Asnwer 1: ", part1())
print("Answer 2: ", part2())