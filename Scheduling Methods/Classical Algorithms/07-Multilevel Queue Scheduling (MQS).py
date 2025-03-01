class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.start_time = -1
        self.waiting_time = 0
        self.turnaround_time = 0

def multilevel_queue_scheduling(queues):
    time = 0
    completed_processes = []

    while any(queues):  # Continue until all queues are empty
        for queue in queues:
            if queue:
                current_process = queue.pop(0)
                if current_process.start_time == -1:
                    current_process.start_time = time
                
                time += current_process.burst_time
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)

    return completed_processes

# Example usage
if __name__ == "__main__":
    queue1 = [
        Process(pid=1, arrival_time=0, burst_time=5, priority=1),
        Process(pid=2, arrival_time=2, burst_time=3, priority=1),
    ]

    queue2 = [
        Process(pid=3, arrival_time=1, burst_time=4, priority=2),
        Process(pid=4, arrival_time=3, burst_time=2, priority=2),
    ]

    queues = [queue1, queue2]  # First queue is higher priority

    completed_processes = multilevel_queue_scheduling(queues)

    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
