# task.py
from uuid import uuid4
import json

class Task:

    FILE_TASK = 'tasks.json'

    TASK_STATUS = {
        0 : "Por Hacer",
        1 : "En Progreso",
        2 : "Terminado"
    }

    def _create_file(self):
        try:
            with open(self.FILE_TASK, 'x') as file:
                file.write('[]')
        except FileExistsError:
            pass

    def _read_file(self):
        with open(self.FILE_TASK, 'r') as file:
            return json.loads(file.read())

    def __init__(self) -> None:
        self._create_file()
        pass

    def add_task(self, title:str):
        if not title:
            print("Title is required")
            return None
        
        task = {
            "id": str(uuid4()),
            "title": title,
            "status": self.TASK_STATUS[0]
        }
        
        all_tasks = self._read_file()
        all_tasks.append(task)

        with open(self.FILE_TASK, 'r+') as file:
            file.write(
                json.dumps(all_tasks)
            )
        return task
    
    def update_task(self, task_id:str, new_title:str, new_status:int):
        all_tasks = self._read_file()
        for task in all_tasks:
            if task['id'] == task_id:
                task['status'] = self.TASK_STATUS[int(new_status)]
                if new_title != "":
                    task['title'] = new_title
                break
        
        with open(self.FILE_TASK, 'r+') as file:
            file.write(
                json.dumps(all_tasks)
            )

    def get_task(self, task_id:str):
        all_tasks = self._read_file()
        return [task for task in all_tasks if task['id'] == task_id]

    def list_tasks(self):
        return self._read_file()