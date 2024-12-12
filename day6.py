nTest = 130
nLines = 130
grid = []
for i in range(nLines):
    # lst = list(input())
    lst = input()
    if '^' in lst:
        currI = i
        currJ = lst.index('^')
        start = (currI, currJ)
        
    grid.append(lst)

def getPath(grid, start, dir, addedObstruction = None):
    visited = set()
    posVector = set()
    i = start[0]
    j = start[1]
    dx = dir[0]
    dy = dir[1]
    posVector.add((i, j, (dx, dy)))

    while i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
        visited.add((i, j))
        if i+dy >= 0 and j+dx >= 0 and i+dy < len(grid) and j+dx < len(grid[0]) and  (grid[i+dy][j+dx] == "#" or (addedObstruction and (i+dy, j+dx)==addedObstruction)):
            if dx==0:
                dx, dy = -dy, 0
            else:
                dx, dy = 0, dx
        else:
            i, j = i+dy, j+dx
        if (i, j, (dx, dy)) in posVector:
            return True, visited
        posVector.add((i, j, (dx, dy)))
    return False, visited

_, ans = getPath(grid, start, (0, -1))
print("Answer 1: ", len(ans))

count = 0
newPath = ans - {start}
for pos in newPath:
    cycle, _ = getPath(grid, start, (0, -1), pos)
    if cycle:
        count += 1
print("Answer 2: ", count)