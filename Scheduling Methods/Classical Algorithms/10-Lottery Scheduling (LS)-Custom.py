import random
import pandas as pd

# Define the Task class to represent each task
class Task:
    def __init__(self, task_id, tickets, arrival_time, burst_time):
        self.task_id = task_id  # Task ID
        self.tickets = tickets  # Number of lottery tickets assigned to the task
        self.arrival_time = arrival_time  # Time when the task arrives
        self.burst_time = burst_time  # Time required to execute the task (burst time)
        self.remaining_time = burst_time  # Remaining time for the task to execute
        self.execution_time = 0  # Time the task has been executed so far
        self.completed = False  # Flag to track if the task is completed

# Function to read and process the Google Borg dataset
def read_and_process_dataset(file_path):
    df = pd.read_csv(file_path)  # Load the dataset

    tasks = []
    for index, row in df.iterrows():
        task_id = row['Task_ID']  # Extract Task ID
        tickets = row['Priority']  # Assign tickets based on Task Priority (can be customized)
        arrival_time = row['Arrival_Time']  # Task arrival time
        burst_time = row['Processing_Time']  # Task processing time

        tasks.append(Task(task_id, tickets, arrival_time, burst_time))
    
    return tasks

# Lottery Scheduling algorithm
def lottery_scheduling(tasks, total_time):
    total_tickets = sum(task.tickets for task in tasks)  # Total tickets in the system
    scheduled_tasks = []  # List to store the scheduled tasks at each time unit

    # Simulate the lottery for each time unit
    for _ in range(total_time):
        winning_ticket = random.randint(1, total_tickets)  # Draw a random ticket
        current_ticket_sum = 0
        selected_task = None

        # Select the task based on the lottery
        for task in tasks:
            current_ticket_sum += task.tickets
            if winning_ticket <= current_ticket_sum:
                selected_task = task
                break

        # Execute the selected task
        if selected_task and selected_task.remaining_time > 0:
            selected_task.remaining_time -= 1
            selected_task.execution_time += 1
            if selected_task.remaining_time == 0:
                selected_task.completed = True  # Mark task as completed when remaining time is 0
            scheduled_tasks.append(selected_task.task_id)  # Add the task ID to the schedule
        else:
            scheduled_tasks.append(None)  # If no task is selected, mark idle time

    return scheduled_tasks

# Example usage
if __name__ == "__main__":
 
    file_path = 'google_borg_dataset.csv' 

    # Read and process the dataset
    tasks = read_and_process_dataset(file_path)

    # Set the total time for the scheduling (this should be calculated based on your system or dataset)
    total_time = 50  # Example: Total number of time units for scheduling

    # Run the Lottery Scheduling algorithm
    scheduled_tasks = lottery_scheduling(tasks, total_time)

    # Print the scheduled tasks and their times
    print("Scheduled Tasks:")
    for i in range(total_time):
        task_id = scheduled_tasks[i]
        if task_id:
            print(f"Time {i}: Task {task_id}")
        else:
            print(f"Time {i}: Idle")
