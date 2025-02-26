import math

class Task:
    def __init__(self, task_id, execution_time, period):
        self.task_id = task_id
        self.execution_time = execution_time
        self.period = period
        self.remaining_time = execution_time
        self.deadline = period
        self.completed = False

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def calculate_hyperperiod(tasks):
    hyperperiod = tasks[0].period
    for task in tasks[1:]:
        hyperperiod = lcm(hyperperiod, task.period)
    return hyperperiod

def rate_monotonic_scheduling(tasks):
    hyperperiod = calculate_hyperperiod(tasks)
    time = 0
    scheduled_tasks = []

    while time < hyperperiod:
        current_task = None

        for task in sorted(tasks, key=lambda x: x.period):
            if time % task.period == 0:
                task.remaining_time = task.execution_time
                task.deadline = time + task.period

            if task.remaining_time > 0 and (current_task is None or task.period < current_task.period):
                current_task = task

        if current_task:
            current_task.remaining_time -= 1
            scheduled_tasks.append(current_task.task_id)
            if current_task.remaining_time == 0:
                current_task.completed = True
        else:
            scheduled_tasks.append(None)

        time += 1

    return scheduled_tasks, hyperperiod

# Example usage
if __name__ == "__main__":
    tasks = [
        Task(task_id=1, execution_time=1, period=4),
        Task(task_id=2, execution_time=2, period=6),
        Task(task_id=3, execution_time=3, period=8)
    ]

    scheduled_tasks, hyperperiod = rate_monotonic_scheduling(tasks)

    print("Scheduled Tasks:")
    for i in range(hyperperiod):
        task_id = scheduled_tasks[i]
        if task_id:
            print(f"Time {i}: Task {task_id}")
        else:
            print(f"Time {i}: Idle")
