from tkinter import *

root = Tk()
root.title("To-Do List")

row_num = 5
tasks = []

greeting = Label(root, text="TO-DO LIST", font=("Helvetica", 24, "bold"), pady=20)
greeting.grid(row=0, column=0, columnspan=4)

enterTask = Label(root, text="Enter Task:",font=("Arial", 12))
enterTask.grid(row=1, column=0)

e = Entry(root, width=35, borderwidth=1)
e.grid(row=1, column=1, columnspan=2)

tasks_label = Label(root, text="Tasks:", font=("Arial", 12))
tasks_label.grid(row=3, column=0, pady=10)

task_frame = Frame(root)
task_frame.grid(row=4, column=0, columnspan=4)

# Add Task function
def addBut():
    global row_num
    task = e.get()

    if task != "":
        var = IntVar()

        cb = Checkbutton(task_frame, text=task, variable=var, font=("Arial", 11))
        cb.grid(row=row_num, column=0, sticky="w")

        tasks.append((cb, var))
        row_num += 1

        e.delete(0, END)

# Update selected task
def updBut():
    new_task = e.get()

    if new_task != "":
        for cb, var in tasks:
            if var.get() == 1:
                cb.config(text=new_task)
                e.delete(0, END)
                break

butAdd = Button(root, text="Add Task", command=addBut,font=("Arial", 11,))
butAdd.grid(row=2, column=1, pady=10)

butUpd = Button(root, text="Update Task", command=updBut,font=("Arial", 11,))
butUpd.grid(row=2, column=2, pady=10)

root.mainloop()