class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        """
        Add a task with a given priority.
        """
        self.tasks.append((task, priority))
        self.tasks.sort(key=lambda x: x[1], reverse=True)

    def get_next_task(self):
        """
        Retrieve the next task to be executed.
        """
        if self.tasks:
            return self.tasks.pop()[0]
        else:
            return None

# Example usage:
if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task("Task1", 3)
    scheduler.add_task("Task 2", 1)
    scheduler.add_task("Task 3", 2)

    next_task = scheduler.get_next_task()
    while next_task:cd