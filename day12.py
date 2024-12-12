nLines = 140
# nLines = 10
# nLines = 6
# nLines = 4
grid = []
for i in range(nLines):
    grid.append(list(input()))

visited = [[False for j in range(len(grid[0]))] for i in range(nLines)]

traversedArea = {}
traversedPerim = {}
traversedSides = {}

total = 0
total2 = 0

countedTop = set()
countedBottom = set()
countedLeft = set()
countedRight = set()
def isEdge(x, y, countedDir):
    if countedDir==countedLeft:
        if y > 0 and grid[x][y-1]==grid[x][y]:
            return False
    if countedDir==countedRight:
        if y < len(grid[0])-1 and grid[x][y+1] == grid[x][y]:
            return False
    if countedDir==countedTop:
        if x > 0 and grid[x-1][y] == grid[x][y]:
            return False
    if countedDir==countedBottom:
        if x < len(grid)-1 and grid[x+1][y] == grid[x][y]:
            return False
    return True

def counted(countedDir, x, y, dx, dy):
    while(x+dx >= 0 and x+dx < len(grid) and y+dy >= 0 and y+dy < len(grid[0])):
        if (x+dx, y+dy) in countedDir:
            return True
        if grid[x][y] == grid[x+dx][y+dy] and not isEdge(x+dx, y+dy, countedDir):
            return False
        if grid[x][y] != grid[x+dx][y+dy]:
            return False
        x += dx
        y += dy
    return False

def identifyRegions(i, j):
    if visited[i][j] == False:
        traversedArea[grid[i][j]] = traversedArea.get(grid[i][j], 0) + 1
        indSides = 0
        contiguousSides = 0
        
        if i==0 or (i > 0 and grid[i-1][j] != grid[i][j]):
            indSides += 1
            contiguousSides += 1
            if (j > 0 and counted(countedTop, i, j, 0, -1)) or (j < len(grid[0])-1 and counted(countedTop, i, j, 0, 1)):
                contiguousSides -= 1
            countedTop.add((i, j))
            
        if i == len(grid) -1 or (i < len(grid)-1 and grid[i+1][j] != grid[i][j]):
            indSides += 1
            contiguousSides += 1
            if (j > 0 and counted(countedBottom, i, j, 0, -1)) or (j < len(grid[0])-1 and counted(countedBottom, i, j, 0, 1)):
                contiguousSides -= 1
            countedBottom.add((i, j))
            
        if j == len(grid[0])-1 or (j < len(grid[0])-1 and grid[i][j+1] != grid[i][j]):
            indSides += 1
            contiguousSides += 1
            if (i > 0 and counted(countedRight, i, j, -1, 0)) or (i < len(grid)-1 and counted(countedRight, i, j, 1, 0)):
                contiguousSides -= 1
            countedRight.add((i, j))
                        
        if j == 0 or (j > 0 and grid[i][j-1] != grid[i][j]):
            indSides += 1
            contiguousSides += 1
            if (i > 0 and counted(countedLeft, i, j, -1, 0)) or (i < len(grid)-1 and counted(countedLeft, i, j, 1, 0)):
                contiguousSides -= 1
            countedLeft.add((i, j))

        traversedPerim[grid[i][j]] = traversedPerim.get(grid[i][j], 0) + indSides
        traversedSides[grid[i][j]] = traversedSides.get(grid[i][j], 0) + contiguousSides
       
    visited[i][j] = True
    if i > 0 and grid[i-1][j] == grid[i][j] and not visited[i-1][j]:
        identifyRegions(i-1, j)
    if i < len(grid)-1 and grid[i+1][j] == grid[i][j] and not visited[i+1][j]:
        identifyRegions(i+1, j)
    if j < len(grid[0])-1 and grid[i][j+1] == grid[i][j] and not visited[i][j+1]:
        identifyRegions(i, j+1)
    if j > 0 and grid[i][j-1] == grid[i][j] and not visited[i][j-1]:
        identifyRegions(i, j-1)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not visited[i][j]:
            identifyRegions(i, j)
            
            total += (traversedArea[grid[i][j]] * traversedPerim[grid[i][j]])
            total2 += (traversedArea[grid[i][j]] * traversedSides[grid[i][j]])

            traversedArea = {}
            traversedPerim = {}
            traversedSides = {}
            countedLeft.clear()
            countedRight.clear()
            countedTop.clear()
            countedBottom.clear()

          

print("Answer 1: ", total)
print("Answer 2: ", total2)


