task=[]
next_id=1
print("=======WELCOME TO DO LIST========")
while True:
    print("\n1. Add a tasks")
    print("2. View all tasks")
    print("3. Mark tasks")
    print("4. Delete tasks")
    print("5.Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid menu option.")
        continue

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice! Please select between 1 and 5.")
        continue
    if choice == 5:
        print("Thank you for using To-Do List!!")
        print("Exiting !!!")
        break
    if choice == 1 :
        t_name=input("Enter task name: ").strip()
        if not t_name:
            print("task name cannot be empty!!")
        else:
            d={ "id" : next_id,
               "name" : t_name,
               "status" : "pending"
               }
            task.append(d)
            print("Task Added Successfully!!")
            next_id+=1

    if choice == 2:
        if not task:
              print("No Tasks Available!!")
        else :
            for t in task :
                print(f"ID : {t['id']}")
                print(f"Task Name : {t['name']}")
                print(f"Status : {t['status']}")
                print("--------------------------")

    if choice == 3:
        try:
            t_id=int(input("Enter task id: "))
        except ValueError:
            print("Invalid Input!! Please enter numeric values..")
            continue
        found=False
        for i in task :
            if t_id == i['id']:
                i["status"] = "completed"
                found=True
                print("Task Marked Successfully!!")
                break

        if not found:
            print("Task Not Found!!")
                    
    if choice == 4:
        try:
            t_id=int(input("Enter task id: "))
        except ValueError:
            print("Invalid Input!! Please enter numeric values..")
            continue
        found=False
        for i in task :
            if t_id == i['id']:
                task.remove(i)
                found=True
                print("Task Remove Successfully!!")
                break
    
        if not found:
            print("Task Not Found!!")
                        
    