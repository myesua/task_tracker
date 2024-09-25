from os import path
from datetime import datetime
import json

class TaskAdmin:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        if path.exists(self.tasks_file):
            with open(self.tasks_file, 'r') as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        with open(self.tasks_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    # TODO: make sure todo with same description is not added, or just override existing one if description exists
    def add_task(self, description):
        timestamp = datetime.now().isoformat()
        new_task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "status": "todo",
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }
        self.tasks.append(new_task)
        self.save_tasks() # save tasks to file
        print(f"Task with id - {new_task["id"]} added successfully!")
    
    def update_task(self, task_id, description):
        index = next((i for i, item in enumerate(self.tasks) if item['id'] == task_id), None)
        task_to_update = self.tasks[index]
        if task_to_update:
            task_to_update.update({"description": description, "updatedAt": datetime.now().isoformat()})
            self.save_tasks() # save tasks to file
            print(f"Task with the id - {task_id} has been updated.")
            return
        print(f"No task with the id - {task_id}.")
        
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks() # save tasks to file
        print(f"Task with the id - {task_id} has been removed.")
        
    def list_tasks(self, status=None):
        tasks = self.tasks
        if status:
            print('Tasks: ')
            if any(task["status"] == status for task in tasks):
                for index, task in enumerate(tasks, 1):
                    if task["status"] == status: 
                        print(f"{index}. {task}")
                return
            print(f'No task found with the status - {status}')
            return
        else:
            print('Tasks: ')
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")       
            
    def mark_in_progress(self, task_id):
        index = next((i for i, item in enumerate(self.tasks) if item['id'] == task_id), None)
        task_to_update = self.tasks[index]
        if task_to_update:
            task_to_update.update({"status": "in-progress", "updatedAt": datetime.now().isoformat()})
            self.save_tasks()
            print(f"Task with the id - {task_id} has been updated.")
            return
        print(f"No task with the id - {task_id}.")
        
    def mark_as_done(self, task_id):
        task_to_update = next((task for task in self.tasks if task['id'] == task_id), None)
        if task_to_update:
            task_to_update.update({"status": "done", "updatedAt": datetime.now().isoformat()})
            self.save_tasks()
            print(f"Task with the id - {task_id} has been updated.")
            return
        print(f"No task with the id - {task_id}.")