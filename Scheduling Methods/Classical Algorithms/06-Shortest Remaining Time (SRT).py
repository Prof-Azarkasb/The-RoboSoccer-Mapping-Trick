import heapq

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.start_time = -1
        self.waiting_time = 0
        self.turnaround_time = 0

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time

def shortest_remaining_time(process_list):
    process_list.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    time = 0
    ready_queue = []
    completed_processes = []
    n = len(process_list)

    while len(completed_processes) < n:
        while process_list and process_list[0].arrival_time <= time:
            heapq.heappush(ready_queue, process_list.pop(0))

        if ready_queue:
            current_process = heapq.heappop(ready_queue)
            if current_process.start_time == -1:
                current_process.start_time = time

            time += 1
            current_process.remaining_time -= 1

            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)
            else:
                heapq.heappush(ready_queue, current_process)
        else:
            time += 1

    return completed_processes

# Example usage
if __name__ == "__main__":
    processes = [
        Process(pid=1, arrival_time=0, burst_time=8),
        Process(pid=2, arrival_time=1, burst_time=4),
        Process(pid=3, arrival_time=2, burst_time=9),
        Process(pid=4, arrival_time=3, burst_time=5),
    ]

    completed_processes = shortest_remaining_time(processes)

    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
