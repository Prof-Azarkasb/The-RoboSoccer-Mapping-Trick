import pandas as pd

# Define the Process class to store task information
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid  # Task ID
        self.arrival_time = arrival_time  # Task arrival time
        self.burst_time = burst_time  # Required processing time
        self.priority = priority  # Priority level (lower value = higher priority)
        self.completion_time = 0  # Completion time
        self.turnaround_time = 0  # Turnaround time
        self.waiting_time = 0  # Waiting time

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load dataset

    processes = []
    for index, row in df.iterrows():
        pid = row['Task_ID']  # Extract Task ID
        arrival_time = row['Arrival_Time']  # Extract arrival time
        burst_time = row['Processing_Time']  # Extract processing time
        priority = row['Task_Priority']  # Extract priority level

        processes.append(Process(pid, arrival_time, burst_time, priority))
    
    return processes

# Priority Scheduling Algorithm Implementation
def priority_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    processes.sort(key=lambda x: (x.arrival_time, x.priority))  # Initial sorting by arrival time and priority

    while completed != n:
        idx = -1
        max_priority = float('inf')

        # Select the highest priority task that has arrived
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
            time += 1  # Increment time if no task is ready

    # Print the results
    print("PID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.priority}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Execution
if __name__ == "__main__":
    file_path = 'google_borg_dataset.csv'
    processes = read_and_process_dataset(file_path)
    priority_scheduling(processes)
