import pandas as pd
import heapq

# Define the Task class to store task information
class Task:
    def __init__(self, pid, deadline, processing_time):
        self.pid = pid  # Task ID
        self.deadline = deadline  # Deadline of the task
        self.processing_time = processing_time  # Task's processing time

    def __lt__(self, other):
        # Comparison function for sorting tasks by their deadline
        return self.deadline < other.deadline

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load the dataset

    tasks = []
    for index, row in df.iterrows():
        pid = row['Task_ID']  # Extract Task ID
        deadline = row['End_Time']  # Assuming 'End_Time' is the deadline (as per your paper's feature mapping)
        processing_time = row['Processing_Time']  # Processing time

        tasks.append(Task(pid, deadline, processing_time))
    
    return tasks

# EDF Scheduling Algorithm Implementation
def earliest_deadline_first(tasks):
    # Convert tasks to a min-heap based on their deadlines
    heapq.heapify(tasks)
    current_time = 0
    schedule = []

    # Process tasks based on their deadlines
    while tasks:
        task = heapq.heappop(tasks)
        schedule.append((task.pid, current_time, current_time + task.processing_time))
        current_time += task.processing_time

    return schedule

# Execution
if __name__ == "__main__":
    # File path to your Google Borg dataset
    file_path = 'google_borg_dataset.csv'  
    tasks = read_and_process_dataset(file_path)
    
    # Apply EDF scheduling
    schedule = earliest_deadline_first(tasks)

    # Print the results
    print("Task ID\tStart Time\tEnd Time")
    for task in schedule:
        print(f"{task[0]}\t{task[1]}\t\t{task[2]}")
