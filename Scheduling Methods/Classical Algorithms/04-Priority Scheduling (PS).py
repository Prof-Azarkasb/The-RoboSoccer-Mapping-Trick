class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def priority_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    
    while completed != n:
        idx = -1
        max_priority = float('inf')
        for i in range(n):
            if processes[i].arrival_time <= time and not is_completed[i]:
                if processes[i].priority < max_priority:
                    max_priority = processes[i].priority
                    idx = i
                if processes[i].priority == max_priority:
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
    print("PID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.priority}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 6, 2),
        Process(2, 2, 8, 1),
        Process(3, 4, 7, 4),
        Process(4, 5, 3, 3)
    ]
    priority_scheduling(processes)