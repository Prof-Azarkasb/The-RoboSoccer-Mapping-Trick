import random

class Task:
    def __init__(self, task_id, tickets):
        self.task_id = task_id
        self.tickets = tickets
        self.execution_time = 0

def lottery_scheduling(tasks, total_time):
    total_tickets = sum(task.tickets for task in tasks)
    scheduled_tasks = []

    for _ in range(total_time):
        winning_ticket = random.randint(1, total_tickets)
        current_ticket_sum = 0
        selected_task = None

        for task in tasks:
            current_ticket_sum += task.tickets
            if winning_ticket <= current_ticket_sum:
                selected_task = task
                break

        selected_task.execution_time += 1
        scheduled_tasks.append(selected_task.task_id)

    return scheduled_tasks

# Example usage
if __name__ == "__main__":
    tasks = [
        Task(task_id=1, tickets=10),
        Task(task_id=2, tickets=20),
        Task(task_id=3, tickets=30)
    ]
    
    total_time = 50
    scheduled_tasks = lottery_scheduling(tasks, total_time)

    print("Scheduled Tasks:")
    for i in range(total_time):
        print(f"Time {i}: Task {scheduled_tasks[i]}")
