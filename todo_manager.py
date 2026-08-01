tasks = []
def add_task(t): tasks.append(t)
def list_tasks():
    for i, t in enumerate(tasks):
        print(f'{i+1}. {t}')