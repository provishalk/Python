def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] = 0
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "       \t\t", processSize[i],end="  \t   \t \t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    m = int(input("Enter Number of Block Size:"))
    print("Enter Block Size:")
    blockSize = []
    for i in range(m):
        blockSize.append(int(input(':')))

    n = int(input("Enter Number of Process Size:"))
    processSize = []
    print("Enter process Size:")
    for j in range(n):
        processSize.append(int(input(':')))

    bestFit(blockSize, m, processSize, n)
