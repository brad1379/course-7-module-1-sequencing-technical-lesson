from tasks.task_manager import display_tasks, filter_tasks, task_generator

# Initial list of tasks
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]

print("\nAll Tasks:")
display_tasks(tasks)

filter_tasks(tasks, "project")

project_tasks = task_generator(tasks, "project")
print(next(project_tasks))