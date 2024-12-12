files = input().strip()
fileFormat = [(None if i%2 else i//2, int(d)) for i, d in enumerate(files)]

def sortFile(file):
    for i in range(len(file)-1, -1, -1):
        for j in range(i):
            iData, iSize = file[i]
            jData, jSize = file[j]
            if (jData==None) and iData and iSize <= jSize:
                file[i] = (None, iSize)
                file[j] = (None, jSize - iSize)
                file.insert(j, (iData, iSize))
                break
    return file



fileFormat = sortFile(fileFormat)
sum = 0
idx = 0
for i in range(len(fileFormat)):
    if fileFormat[i][0] != None:
        data, size = fileFormat[i]
        for j in range(size):
            sum += (data*idx)
            idx += 1
    else:
        idx += fileFormat[i][1]


print("Answer 2: ", sum)
        

