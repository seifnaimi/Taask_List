from typing import List, Tuple

class Task:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.is_done = False

    def mark_as_done(self) -> None:
        self.is_done = True

    def __str__(self) -> str:
        status = "fait" if self.is_done else "pas fait"
        return f"{self.name} - {status}: {self.description}"

class TaskList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, name: str, description: str) -> None:
        task = Task(name, description)
        self.tasks.append(task)

    def mark_task_as_done(self, task_name: str) -> None:
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_done()
                return

    def get_all_tasks(self) -> List[str]:
        return [str(task) for task in self.tasks]

    def get_all_not_done_tasks(self) -> List[str]:
        return [str(task) for task in self.tasks if not task.is_done]

    def get_all_done_tasks(self) -> List[str]:
        return [str(task) for task in self.tasks if task.is_done]
        
task_list = TaskList()
task_list.add_task("faire projet taskList", "expliquer le code")
task_list.add_task("faire projet max rover", "expliquer choix des outils")
task_list.mark_task_as_done("projet CI")
print(task_list.get_all_tasks())
print(task_list.get_all_not_done_tasks())
print(task_list.get_all_done_tasks())

"""
Dans ce code, nous avons une classe Task qui représente une tâche individuelle, avec un nom, une description et un état de "fait" ou "pas fait". 
Nous avons également une classe TaskList qui gère une collection de tâche. 
Les méthode de la classe TaskList permettent d'ajouter des tâches, 
de marquer des tâches comme terminés et de récupérer des sous-ensembles de tâches en fonction de leur statut. 

"""
