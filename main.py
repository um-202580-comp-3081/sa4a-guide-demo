from task_manager import TaskManager

def main():
    manager = TaskManager()

    manager.add_task("Write documentation", "Update README with usage instructions", "High")
    manager.add_task("Fix bug in login", "Handle empty password case")
    manager.add_task("Review pull request", priority="Low")

    print("\nPending Tasks:")

    for task in manager.get_pending_tasks():
        print(f"    {task}")
    
    manager.tasks[0].complete()

    print(f"\nNumber of completed tasks: {len(manager.get_completed_tasks())}")
    print(f"Number of pending tasks: {len(manager.get_pending_tasks())}")

if __name__ == "__main__":
    main()
