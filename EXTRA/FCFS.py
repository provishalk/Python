
def findWaitingTime(processes, n, bt, wt, at):
    ST = [0] * n
    ST[0] = 0
    wt[0] = 0
    for i in range(1, n):
        ST[i] = (ST[i - 1] + bt[i - 1])
        wt[i] = ST[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
def findavgTime(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, bt, wt, at)

    findTurnAroundTime(processes, n, bt, wt, tat)

    print("  P\t\t\tB.T\t\t A.T\tW.T\t\tT.A Time\t  C.T \n")
    TWT= 0
    T_TAT = 0
    for i in range(n):
        TWT= TWT+ wt[i]
        T_TAT = T_TAT + tat[i]
        CT = tat[i] + at[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],"\t\t", wt[i], "\t\t ", tat[i], "\t\t ", CT)

    print("Average waiting time = %.5f " % (TWT/ n))
    print("\nAverage turn around time = ", T_TAT / n)

if __name__ == "__main__":
    processes = [1, 2, 3,4,5]
    n = 5
    burst_time = [5, 9, 6,1,2]
    arrival_time = [0, 3, 4,1,2]

    findavgTime(processes, n, burst_time,arrival_time)

