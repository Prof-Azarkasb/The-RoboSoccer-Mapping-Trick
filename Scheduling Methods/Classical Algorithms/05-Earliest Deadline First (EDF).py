import heapq

class Task:
    def __init__(self, name, deadline, duration):
        self.name = name
        self.deadline = deadline
        self.duration = duration

    def __lt__(self, other):
        return self.deadline < other.deadline

def earliest_deadline_first(tasks):
    heapq.heapify(tasks)
    current_time = 0
    schedule = []

    while tasks:
        task = heapq.heappop(tasks)
        schedule.append((task.name, current_time, current_time + task.duration))
        current_time += task.duration

    return schedule

# Example usage
if __name__ == "__main__":
    tasks = [
        Task('Task 1', 4, 2),
        Task('Task 2', 2, 1),
        Task('Task 3', 6, 2),
        Task('Task 4', 8, 1)
    ]

    schedule = earliest_deadline_first(tasks)

    print("Task\tStart Time\tEnd Time")
    for task in schedule:
        print(f"{task[0]}\t{task[1]}\t\t{task[2]}")
