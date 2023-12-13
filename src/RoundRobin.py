if __name__ == '__main__':
    # Python program for implementation of RR Scheduling
    print("Enter Total Process Number:")
    total_p_no = int(input())
    total_time = 0
    total_time_counted = 0
    # proc is a process list
    proc = []
    wait_time = 0
    turnaround_time = 0

    # Getting the input for each process using list comprehension
    proc = [[int(x) for x in input("Enter process arrival time and burst time: ").split()] for _ in range(total_p_no)]

    # total_time gets incremented with the burst time of each process
    total_time = sum(process[1] for process in proc)

    print("Enter time quantum:")
    time_quantum = int(input())

    # Keep traversing in a round-robin manner until total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            # proc[i][2] here refers to remaining_time for each process i.e., "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                # the process has completely ended here, thus setting its remaining time to 0.
                proc[i][2] = 0
            elif proc[i][2] > 0:
                # if the process has not finished, decrementing its remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
                if proc[i][2] == 0 and proc[i][3] != 1:
                    # if remaining time of process is 0
                    # and individual waiting time of the process has not been calculated i.e., flag
                    wait_time += total_time_counted - proc[i][0] - proc[i][1]
                    turnaround_time += total_time_counted - proc[i][0]
                    # flag is set to 1 once wait time is calculated
                    proc[i][3] = 1

    # Print average waiting time and average turnaround time outside the loop
    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)
