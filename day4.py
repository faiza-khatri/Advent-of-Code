wordSearch = []
for i in range(140):
    lst = list(input().strip())
    wordSearch.append(lst)

possibilities = ["XMAS", "SAMX"]
answers = set()  

def check_match(x, y, dx, dy):
    word = ""
    coordinates = []
    for step in range(4):
        word += wordSearch[x + step * dx][y + step * dy]
        coordinates.append((x + step * dx, y + step * dy))
    if word in possibilities:
        answers.add(tuple(sorted(coordinates)))  


for i in range(len(wordSearch)):
    for j in range(len(wordSearch[i])):
        if i >= 3: 
            check_match(i, j, -1, 0)
        if i >= 3 and j >= 3:  
            check_match(i, j, -1, -1)
        if i >= 3 and j <= len(wordSearch[i]) - 4: 
            check_match(i, j, -1, 1)
        if j >= 3:
            check_match(i, j, 0, -1)
        if j <= len(wordSearch[i]) - 4: 
            check_match(i, j, 0, 1)
        if i <= len(wordSearch) - 4:
            check_match(i, j, 1, 0)
        if i <= len(wordSearch) - 4 and j <= len(wordSearch[i]) - 4:
            check_match(i, j, 1, 1)
        if i <= len(wordSearch) - 4 and j >= 3: 
            check_match(i, j, 1, -1)

count = 0
possibilties = ["MS", "SM"]
for i in range(1, len(wordSearch)-1):
    for j in range(1, len(wordSearch)-1):
        if wordSearch[i][j] == 'A':
            if wordSearch[i-1][j-1]+wordSearch[i+1][j+1] in possibilties and wordSearch[i-1][j+1]+wordSearch[i+1][j-1] in possibilties:
                count +=1 
print("Answer 1 : ", len(answers))
print("Answer 2 : ", count)

