import heapq
import pandas as pd

# Define the Process class to represent each task
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Task ID
        self.arrival_time = arrival_time  # Arrival time of the task
        self.burst_time = burst_time  # Total burst time
        self.remaining_time = burst_time  # Remaining time for the task to execute
        self.completion_time = 0  # Completion time for the task
        self.start_time = -1  # Start time of the task
        self.waiting_time = 0  # Waiting time for the task
        self.turnaround_time = 0  # Turnaround time for the task

    def __lt__(self, other):
        # Comparison function for heapq to prioritize tasks with less remaining time
        return self.remaining_time < other.remaining_time

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load the dataset

    processes = []
    for index, row in df.iterrows():
        pid = row['Task_ID']  # Extract Task ID
        arrival_time = row['Arrival_Time']  # Arrival time
        burst_time = row['Processing_Time']  # Processing time (Burst time)

        processes.append(Process(pid, arrival_time, burst_time))
    
    return processes

# Shortest Remaining Time (SRT) Scheduling Algorithm Implementation
def shortest_remaining_time(process_list):
    process_list.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    time = 0  # Start time of the system
    ready_queue = []  # Min-heap to manage ready processes based on remaining time
    completed_processes = []  # List to track completed processes
    n = len(process_list)

    while len(completed_processes) < n:
        # Add all processes that have arrived at the current time to the ready queue
        while process_list and process_list[0].arrival_time <= time:
            heapq.heappush(ready_queue, process_list.pop(0))

        if ready_queue:
            # Get the process with the shortest remaining time
            current_process = heapq.heappop(ready_queue)

            if current_process.start_time == -1:
                current_process.start_time = time

            # Execute the process for 1 unit of time
            time += 1
            current_process.remaining_time -= 1

            # If the process has finished, calculate its metrics
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)
            else:
                heapq.heappush(ready_queue, current_process)
        else:
            time += 1  # If no process is ready, increment time

    return completed_processes

# Example usage
if __name__ == "__main__":
 
    file_path = 'google_borg_dataset.csv'
    processes = read_and_process_dataset(file_path)
    
    # Apply Shortest Remaining Time scheduling
    completed_processes = shortest_remaining_time(processes)

    # Print the results
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
