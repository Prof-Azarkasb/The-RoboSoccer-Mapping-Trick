class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def sjn_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    processes.sort(key=lambda x: x.arrival_time)
    
    while completed != n:
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if processes[i].arrival_time <= time and not is_completed[i]:
                if processes[i].burst_time < min_burst:
                    min_burst = processes[i].burst_time
                    idx = i
                if processes[i].burst_time == min_burst:
                    if processes[i].arrival_time < processes[idx].arrival_time:
                        idx = i
        if idx != -1:
            processes[idx].completion_time = time + processes[idx].burst_time
            processes[idx].turnaround_time = processes[idx].completion_time - processes[idx].arrival_time
            processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
            time += processes[idx].burst_time
            is_completed[idx] = True
            completed += 1
        else:
            time += 1

    # Print the results
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 6),
        Process(2, 2, 8),
        Process(3, 4, 7),
        Process(4, 5, 3)
    ]
    sjn_scheduling(processes)
