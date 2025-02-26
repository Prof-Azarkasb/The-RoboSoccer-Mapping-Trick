import pandas as pd
import heapq

# Define the Process class to represent each task
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid  # Task ID
        self.arrival_time = arrival_time  # Arrival time of the task
        self.burst_time = burst_time  # Total burst time
        self.remaining_time = burst_time  # Remaining time for the task to execute
        self.priority = priority  # Priority of the task
        self.completion_time = 0  # Completion time for the task
        self.start_time = -1  # Start time of the task
        self.waiting_time = 0  # Waiting time for the task
        self.turnaround_time = 0  # Turnaround time for the task

    def __lt__(self, other):
        # Comparison function for heapq to prioritize tasks with less remaining time
        return self.priority < other.priority

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load the dataset

    processes = []
    for index, row in df.iterrows():
        pid = row['Task_ID']  # Extract Task ID
        arrival_time = row['Arrival_Time']  # Arrival time
        burst_time = row['Processing_Time']  # Processing time (Burst time)
        priority = row['Priority']  # Priority for the task (customized feature)

        processes.append(Process(pid, arrival_time, burst_time, priority))
    
    return processes

# Multilevel Queue Scheduling Algorithm Implementation
def multilevel_queue_scheduling(queues):
    time = 0  # Initialize the system time
    completed_processes = []  # List to track completed processes

    while any(queues):  # Continue until all queues are empty
        for queue in queues:
            if queue:
                current_process = queue.pop(0)  # Get the highest-priority process

                if current_process.start_time == -1:
                    current_process.start_time = time  # Set the start time

                # Simulate task execution
                time += current_process.burst_time
                current_process.completion_time = time  # Set completion time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  # Calculate turnaround time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time  # Calculate waiting time

                completed_processes.append(current_process)

    return completed_processes

# Example usage
if __name__ == "__main__":
   
    file_path = 'google_borg_dataset.csv' 

    processes = read_and_process_dataset(file_path)

    # Assuming two priority queues for demonstration
    queue1 = [process for process in processes if process.priority == 1]  # High priority queue
    queue2 = [process for process in processes if process.priority == 2]  # Low priority queue

    queues = [queue1, queue2]  # First queue has higher priority

    completed_processes = multilevel_queue_scheduling(queues)

    # Print the results
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
