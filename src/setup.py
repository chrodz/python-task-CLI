from src.task import Task

class Setup:

    OPTIONS = {
        1: "Add Task",
        2: "Update Task",
        3: "Delete Task",
        4: "List Tasks",
        5: "Exit",
    }

    def __init__(self) -> None:
        pass

    def get_options(self) -> str:
        return "\n".join([f'{k}. {option}' for k,option in self.OPTIONS.items()])
    
    def get_user_input(self):
        user_option = input("Select an option:").strip()

        try:

            if int(user_option) not in list(self.OPTIONS.keys()):
                print("Plase select a valid option...")
                return self.get_user_input()
            else:
                if int(user_option) == 1:
                    self.add_task()
                elif int(user_option) == 2:
                    self.update_task()
                elif int(user_option) == 3:
                    self.delete_task()
                elif int(user_option) == 4:
                    self.list_tasks()
                elif int(user_option) == 5:
                    exit()

                self.get_user_input()
        except ValueError:
            print("Please select a valid option...")
            return self.get_user_input()

    def list_tasks(self):
        tasks = Task().list_tasks()
        for task in tasks:
            print("ID: {0} - Title: {1} - Status: {2}".format(task['id'], task['title'], task['status']))

    def add_task(self):
        title = input("Enter the title of the task:")
        new_task = Task()
        if (task := new_task.add_task(title)) is not None:
            self.print_message("added", task['id'], task['title'])
        else:
            print("Error adding task")

    def update_task(self):
        new_task = Task()
        task_id = input("Enter the task id:")
        task = new_task.get_task(task_id)
        print("Task found: {0}".format(task))
        print("Task status: {0}".format("".join([f'{k}. {option}' for k,option in Task.TASK_STATUS.items()])))

        new_status = input("Enter the new status of the task:")
        new_title = input("Enter the new title of the task:")
        new_task.update_task(task_id, new_title, new_status)
        print("Task updated successfully")

    def get_pending_tasks(self) -> list:
        new_task = Task()
        print(new_task)

        return ""
    
    def print_message(self, method:str, task_id:str, task_title:str) -> None:
        print("###############")
        print('Task {0} {1} successfully'.format(task_title, method))
        print('Task ID: {0}'.format(task_id))
        print("###############")