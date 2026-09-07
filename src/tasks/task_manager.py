def display_tasks(task_list):
    """Displays the list of tasks."""
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def filter_tasks(task_list, keyword):
    filtered_tasks = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"Tasks matching '{keyword}': ")
    display_tasks(filtered_tasks)

def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())