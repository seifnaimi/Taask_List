from task import TaskList


def test_task_list():
    task_list = TaskList()
    task_list.add_task("faire projet taskList", "expliquer le code")
    task_list.add_task("faire projet max rover", "expliquer choix des outils")
    task_list.mark_task_as_done("faire projet taskList")

    tasks = task_list.get_all_tasks()
    not_done_tasks = task_list.get_all_not_done_tasks()
    done_tasks = task_list.get_all_done_tasks()

    # Tester que les bonne tâches sont renvoyés
    assert "faire projet taskList - fait: expliquer le code" in tasks
    assert "faire projet max rover - pas fait: expliquer choix des outils" in tasks
    assert "faire projet taskList - fait: expliquer le code" in done_tasks
    assert "faire projet max rover - pas fait: expliquer choix des outils" in not_done_tasks

"""
Ce code crée une instance de la classe TaskList, ajoute deux tâche, 
marque une tâche comme terminé, puis vérifie que les méthodes get_all_tasks, 
get_all_not_done_tasks et get_all_done_tasks retournent les tâches correcte en utilisant les assert. 

"""
