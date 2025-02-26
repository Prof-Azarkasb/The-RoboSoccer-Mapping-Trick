import math
import pandas as pd

# Define the Task class to represent each task
class Task:
    def __init__(self, task_id, execution_time, period):
        self.task_id = task_id  # Task ID
        self.execution_time = execution_time  # Time required to execute the task
        self.period = period  # Period of the task
        self.remaining_time = execution_time  # Remaining execution time for the task
        self.deadline = period  # Deadline for task completion
        self.completed = False  # Flag to track if the task is completed

# Function to calculate the Least Common Multiple (LCM) for two numbers
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function to calculate the hyperperiod, which is the least common multiple of all periods
def calculate_hyperperiod(tasks):
    hyperperiod = tasks[0].period
    for task in tasks[1:]:
        hyperperiod = lcm(hyperperiod, task.period)
    return hyperperiod

# Function to implement Rate-Monotonic Scheduling (RMS)
def rate_monotonic_scheduling(tasks):
    hyperperiod = calculate_hyperperiod(tasks)  # Calculate the hyperperiod
    time = 0  # Start from time = 0
    scheduled_tasks = []  # List to track the tasks scheduled at each time unit

    while time < hyperperiod:
        current_task = None  # Variable to store the task that will be executed

        # Check if any task is ready to execute at the current time
        for task in sorted(tasks, key=lambda x: x.period):  # Sort tasks by period (shorter period = higher priority)
            if time % task.period == 0:
                task.remaining_time = task.execution_time  # Reset remaining time when the task period starts
                task.deadline = time + task.period  # Set the deadline for the task

            # Choose the task with the highest priority (shortest period)
            if task.remaining_time > 0 and (current_task is None or task.period < current_task.period):
                current_task = task

        # Execute the selected task
        if current_task:
            current_task.remaining_time -= 1  # Reduce the remaining time by 1 unit of time
            scheduled_tasks.append(current_task.task_id)  # Add task ID to the schedule
            if current_task.remaining_time == 0:
                current_task.completed = True  # Mark task as completed when remaining time is 0
        else:
            scheduled_tasks.append(None)  # If no task is scheduled, mark idle time

        time += 1  # Increment time by 1 unit

    return scheduled_tasks, hyperperiod

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load the dataset

    tasks = []
    for index, row in df.iterrows():
        task_id = row['Task_ID']  # Extract Task ID
        execution_time = row['Processing_Time']  # Task processing time
        period = row['Period']  # Task period (this should be a defined column in your dataset)

        tasks.append(Task(task_id, execution_time, period))
    
    return tasks

# Example usage
if __name__ == "__main__":
    # File path to your Google Borg dataset
    file_path = 'google_borg_dataset.csv'  # Replace with your actual dataset path

    # Read and process the dataset
    tasks = read_and_process_dataset(file_path)

    # Run the RMS scheduling algorithm
    scheduled_tasks, hyperperiod = rate_monotonic_scheduling(tasks)

    # Print the scheduled tasks and their times
    print("Scheduled Tasks:")
    for i in range(hyperperiod):
        task_id = scheduled_tasks[i]
        if task_id:
            print(f"Time {i}: Task {task_id}")
        else:
            print(f"Time {i}: Idle")
