## this program calculates : average  waiting time for non primtive process
def CalculateWaitingTime(at,bt,n):
    wt = [0]*n  ## declare an array for the waiting time
    
    ## we know that waiting time for the first program is 0 so set the waiting time to 0 for the first process
    wt[0] = 0
    print("P.No.\tArrival Time\t" , "Burst Time\tWaiting Time")
    print("1" , "\t\t" , at[0] , "\t\t" , bt[0] , "\t\t" , wt[0])


    ##calculating the waiting time for each process
    for i in range(1,5):
        wt[i] = (at[i-1]+bt[i-1]+wt[i-1]-at[i])
        print(i+1,"\t\t",at[i],"\t\t",bt[i],"\t\t",wt[i])
    
    average = 0.0
    sum = 0
    for i in range(5):
        sum = sum + wt[i]
    
    average = sum/5

    print("Average waiting time = ",average)


n = 5
at = [0, 1, 2, 3, 4]
bt = [4, 3, 1, 2, 5]
CalculateWaitingTime(at, bt, n)