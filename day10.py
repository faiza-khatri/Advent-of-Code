def endsAt92(start, pos, grid, visited):
    i, j = pos
    # print("currently at: (", i, j, ")", start)
    sum = 0
    visited[i][j] = True 
    if start == 9:
        return 1
    if i<len(grid)-1 and grid[i+1][j] == start + 1 and not visited[i+1][j]:
        sum += endsAt92(start+1, (i+1, j), grid, visited)
    if i > 0 and grid[i-1][j] == start + 1 and not visited[i-1][j]:
        sum += endsAt92(start+1, (i-1, j), grid, visited)
    if j <len(grid[0])-1 and grid[i][j+1] == start + 1 and not visited[i][j+1]:
        sum += endsAt92(start+1, (i, j+1), grid, visited)
    if j > 0 and grid[i][j-1] == start + 1 and not visited[i][j-1]:
        sum += endsAt92(start + 1, (i, j-1), grid, visited)

    visited[i][j] = False
    return sum

def endsAt9(start, pos, grid):
    i, j = pos
    # print("currently at: (", i, j, ")", start)
    sum = 0
    if start == 9:
        return 1
    if i<len(grid)-1 and grid[i+1][j] == start + 1 :
        sum += endsAt9(start+1, (i+1, j), grid,)
    if i > 0 and grid[i-1][j] == start + 1 :
        sum += endsAt9(start+1, (i-1, j), grid)
    if j <len(grid[0])-1 and grid[i][j+1] == start + 1 :
        sum += endsAt9(start+1, (i, j+1), grid)
    if j > 0 and grid[i][j-1] == start + 1 :
        sum += endsAt9(start + 1, (i, j-1), grid)

    return sum

nLines = 49
# nLines = 8
gridST = []
for i in range(nLines):
    lst = list(map(int, input().strip()))
    gridST.append(lst)
sumOfTrails = 0
sumOfTrails1 = 0
# print(gridST)
for i in range(len(gridST)):
    for j in range(len(gridST[0])):
        if gridST[i][j] == 0:
            visited = [[False] * len(gridST[0]) for _ in range(len(gridST))]
            sumOfTrails += endsAt9(0, (i, j), gridST)
            sumOfTrails1 += endsAt92(0, (i, j), gridST, visited)

print("Answer 1: ",sumOfTrails1)
print("Answer 2: ", sumOfTrails)