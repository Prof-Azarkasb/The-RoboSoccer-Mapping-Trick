import pandas as pd
import queue

# Define the Process class to represent each task
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Task ID
        self.arrival_time = arrival_time  # Arrival time of the task
        self.burst_time = burst_time  # Total burst time
        self.remaining_time = burst_time  # Remaining time for the task to execute
        self.start_time = -1  # Start time of the task
        self.completion_time = 0  # Completion time for the task
        self.waiting_time = 0  # Waiting time for the task
        self.turnaround_time = 0  # Turnaround time for the task
        self.queue_level = 0  # The queue level the task is currently in

    def __lt__(self, other):
        # Comparison function to prioritize tasks with less remaining time (within the same queue)
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

# Multilevel Feedback Queue (MFQ) Scheduling Algorithm Implementation
def multilevel_feedback_queue(process_list, time_quantums):
    queues = [queue.Queue() for _ in time_quantums]  # Create multiple queues with different time quantums
    time = 0  # Initialize the system time
    completed_processes = []  # List to track completed processes

    while process_list or any(not q.empty() for q in queues):
        # Add processes that have arrived at the current time
        for process in process_list[:]:
            if process.arrival_time <= time:
                queues[0].put(process)  # Insert into the highest priority queue
                process_list.remove(process)

        # Process tasks from each queue in round-robin fashion
        for i, quantum in enumerate(time_quantums):
            if not queues[i].empty():
                current_process = queues[i].get()

                if current_process.start_time == -1:
                    current_process.start_time = time  # Set the start time when the process begins execution

                if current_process.remaining_time > quantum:
                    time += quantum  # Simulate task execution for the time quantum
                    current_process.remaining_time -= quantum
                    if i + 1 < len(queues):
                        queues[i + 1].put(current_process)  # Move to the next lower priority queue
                else:
                    time += current_process.remaining_time  # Execute the remaining time of the task
                    current_process.remaining_time = 0  # Task is finished
                    current_process.completion_time = time  # Set completion time
                    current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  # Calculate turnaround time
                    current_process.waiting_time = current_process.turnaround_time - current_process.burst_time  # Calculate waiting time
                    completed_processes.append(current_process)

                break
        else:
            time += 1  # If no process is ready, increment time

    return completed_processes

# Example usage
if __name__ == "__main__":
    
    file_path = 'google_borg_dataset.csv'

    processes = read_and_process_dataset(file_path)

    # Defining different time quantums for each queue level
    # The first queue has the smallest quantum, simulating a higher priority
    time_quantums = [4, 8, 12]  # Different time quantums for each queue level

    # Running the MFQ scheduling algorithm
    completed_processes = multilevel_feedback_queue(processes, time_quantums)

    # Print the results
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
