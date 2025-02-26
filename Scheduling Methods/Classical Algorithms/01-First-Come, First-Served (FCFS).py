class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time = process.completion_time

    # Print the results
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 4),
        Process(2, 1, 3),
        Process(3, 2, 1),
        Process(4, 3, 2)
    ]
    fcfs_scheduling(processes)
