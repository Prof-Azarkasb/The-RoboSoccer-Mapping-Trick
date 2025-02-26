import pandas as pd

# Define the Process class to hold process attributes
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Time when process arrives
        self.burst_time = burst_time  # Time required for task execution
        self.completion_time = 0  # Time when process completes
        self.turnaround_time = 0  # Time from arrival to completion
        self.waiting_time = 0  # Time the process spends waiting in the queue

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    # Read the dataset using pandas
    df = pd.read_csv(file_path)
    
    # Select relevant columns from the dataset
    processes = []
    for index, row in df.iterrows():
        # Example of extracting relevant columns: 'Task_ID', 'Arrival_Time', 'Processing_Time'
        pid = row['Task_ID']  # Assuming 'Task_ID' is the unique identifier in the dataset
        arrival_time = row['Arrival_Time']  # Assuming 'Arrival_Time' column exists
        burst_time = row['Processing_Time']  # Assuming 'Processing_Time' column exists
        processes.append(Process(pid, arrival_time, burst_time))
    
    return processes

# Shortest Job Next Scheduling function
def sjn_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    processes.sort(key=lambda x: x.arrival_time)
    
    while completed != n:
        idx = -1
        min_burst = float('inf')
        
        # Find the process with the shortest burst time that has already arrived
        for i in range(n):
            if processes[i].arrival_time <= time and not is_completed[i]:
                if processes[i].burst_time < min_burst:
                    min_burst = processes[i].burst_time
                    idx = i
                if processes[i].burst_time == min_burst:
                    if processes[i].arrival_time < processes[idx].arrival_time:
                        idx = i
        
        # If a process is found, execute it
        if idx != -1:
            processes[idx].completion_time = time + processes[idx].burst_time
            processes[idx].turnaround_time = processes[idx].completion_time - processes[idx].arrival_time
            processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
            time += processes[idx].burst_time
            is_completed[idx] = True
            completed += 1
        else:
            time += 1  # If no process is ready, increment time

    # Print the results
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Example usage
if __name__ == "__main__":
    file_path = 'google_borg_dataset.csv'
    
    # Read and process the dataset
    processes = read_and_process_dataset(file_path)
    
    # Perform Shortest Job Next scheduling and print the results
    sjn_scheduling(processes)
