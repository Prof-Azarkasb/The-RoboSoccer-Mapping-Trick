import pandas as pd

# Define the Process class to hold process attributes
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Time when process arrives
        self.burst_time = burst_time  # Time required for task execution
        self.remaining_time = burst_time  # Time remaining to execute (initially the burst time)
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

# Round Robin Scheduling function
def round_robin_scheduling(processes, quantum):
    time = 0
    queue = []  # Queue of processes that are ready for execution
    complete = []  # List of completed processes
    
    while processes or queue:
        # Add arriving processes to the queue
        while processes and processes[0].arrival_time <= time:
            queue.append(processes.pop(0))
        
        if queue:
            current_process = queue.pop(0)
            execution_time = min(quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            time += execution_time

            # If the process is completed
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                complete.append(current_process)
            else:
                # Re-queue the process if not completed
                queue.append(current_process)
        else:
            time += 1  # If no process is ready, increment time

    # Print the results
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in sorted(complete, key=lambda x: x.pid):
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Example usage
if __name__ == "__main__":
  
    file_path = 'google_borg_dataset.csv' 
    
    # Read and process the dataset
    processes = read_and_process_dataset(file_path)
    
    # Define Round Robin quantum time
    quantum = 2  # Example quantum time
    
    # Perform Round Robin scheduling and print the results
    round_robin_scheduling(processes, quantum)
