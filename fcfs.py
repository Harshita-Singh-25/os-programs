def fcfs_scheduling(processes):
    n = len(processes)
    
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate completion times
    completion_time[0] = processes[0][1]
    for i in range(1, n):
        completion_time[i] = completion_time[i-1] + processes[i][1]
    
    # Calculate waiting time and turnaround time
    for i in range(n):
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - processes[i][1]
    
    # Calculate total waiting and turnaround time
    total_waiting = sum(waiting_time)
    total_turnaround = sum(turnaround_time)

    # Print the table
    print("\nProcess\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    print("---------------------------------------------------------------")
    for i in range(n):
        process_name = processes[i][0] if isinstance(processes[i][0], str) else f"P{processes[i][0]}"
        print(f"{process_name}\t{processes[i][1]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Print averages
    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")

# Example usage
if __name__ == "__main__":
    # processes = [(Process ID or Name, Burst Time)]
    
    processes = [
        [1, 6],
        [2, 3],
        [3, 8],
        [4, 4]
    ]
    print("FCFS CPU Scheduling ")
    fcfs_scheduling(processes)
