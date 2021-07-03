done = []
notdone = []

while True:
    command = input("Add-(addtask), SetDone-(setdone), List Finished-(listdone), List Unfinished-(listnotdone): ")
    if command.startswith("addtask"):
        notdone.append(command.replace("addtask ", ""))
    elif command.startswith("setdone"):
        taskID = int(command.replace("setdone ", ""))
        value_removed = notdone.pop(taskID)
        done.append(value_removed)
    elif command.startswith("listdone"):
        print(done)
    elif command.startswith("listnotdone"):
        print(notdone)
