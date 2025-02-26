import pandas as pd

# Define the Process class to hold process attributes
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Time when process arrives
        self.burst_time = burst_time  # Time required for task execution
        self.completion_time = 0  # Time when process completes
        self.turnaround_time = 0  # Time from arrival to completion
        self.waiting_time = 0  # Time the process spends waiting in the queue
        self.priority = priority  # Priority of the task (if needed for extension)

# Define the First-Come, First-Served (FCFS) scheduling function
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes based on arrival time
    current_time = 0  # Initialize the current time
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # Wait if the system is idle
        process.completion_time = current_time + process.burst_time  # Set completion time
        process.turnaround_time = process.completion_time - process.arrival_time  # Turnaround time
        process.waiting_time = process.turnaround_time - process.burst_time  # Waiting time
        current_time = process.completion_time  # Update current time

    # Print results for the FCFS scheduling
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Function to read the Google Borg dataset and process it
def read_and_process_dataset(file_path):
    # Read the dataset using pandas
    df = pd.read_csv(file_path)
    
    # Select the relevant columns for scheduling (assuming 'Arrival_Time', 'Burst_Time' are available in dataset)
    processes = []
    for index, row in df.iterrows():
        # Extract relevant data, you can adapt this based on your dataset columns
        pid = row['Task_ID']  # Assuming 'Task_ID' is the unique identifier in the dataset
        arrival_time = row['Arrival_Time']  # Assuming 'Arrival_Time' column exists
        burst_time = row['Burst_Time']  # Assuming 'Burst_Time' column exists
        processes.append(Process(pid, arrival_time, burst_time))
    
    return processes

# Example usage of FCFS scheduling
if __name__ == "__main__":
    file_path = 'google_borg_dataset.csv'
    
    # Read and process the dataset
    processes = read_and_process_dataset(file_path)
    
    # Perform FCFS scheduling and print the results
    fcfs_scheduling(processes)
