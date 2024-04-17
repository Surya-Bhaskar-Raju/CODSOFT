# https://www.linkedin.com/pulse/creating-simple-to-do-list-application-python-guide-daniel-joseph-/

def display_menu():
    print('Menu:')
    print('1. Add task')
    print('2. view tasks')
    print('3. Mark as Done')
    print('4. Exit')
    
    
def add_task(tasks):
    task=input('Enter the task: ')
    tasks.append(task)
    print('Task added successfullly')
    

def view_tasks(tasks):
    print("\nTasks:")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
        
        
def mark_test_done(tasks):
    if not tasks:
        print('NO TASKS>PLEASE ADD SOME FIRST')
        return

    view_tasks(tasks)
    index=int(input('Enter the task to be marked:'))-1
    
    if 0<= index < len(tasks):
        removed_task=tasks.pop(index)
        print(f'Task {removed_task} is marked as done and removed')
        
    else:
        print('Invalid ask index')
        
    
def save_tasks(tasks):
    with open('tasks.txt','w') as f:
        for task in tasks:
            f.write(task+'\n')
            
            
def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    

def main():
    tasks=load_tasks()
    
    while True:
        
        print('\n\n')
        display_menu()
        choice=input("Enter your choice:\n")
        
        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            view_tasks(tasks)
        elif choice=='3':
            mark_test_done(tasks)
        elif choice=='4':
            print('Exiting...')
            save_tasks(tasks)
            break
        else:
            print('Invalid choice.Please select again')
            
if __name__=='__main__':
    main()
        
            
            
            
          