import tkinter as tk
from tkinter import ttk
import json
import re


root = tk.Tk()
root.title("TASKS-MANAGER")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.8)

root.geometry(f"{window_width}x{window_height}")
root.configure(bg="#DCDCDC")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# globals
categories = ["Work", "Studies", "Personal", "Miscellaneous"]


class button(tk.Button):  # create default button
    def __init__(self, parent, text, command=None):
        super().__init__(parent, text=text, bg="#00796B", fg="white", font=("Arial", 12), width=15, height=2,
                         relief="flat", command=command)
        self.bind("<Enter>", lambda e: self.config(bg="#5F9EA0"))
        self.bind("<Leave>", lambda e: self.config(bg="#008B8B"))


class label(tk.Label):  # create default label
    def __init__(self, parent, text, size):
        super().__init__(parent, text=text, bg="#DCDCDC", font=("Arial", size))


def temporary_message(frame, text, row, column):  # create temprary message that dissapeared after 3sec
    message = tk.Label(frame, text=text)
    message.grid(row=row, column=column)
    message.after(3000, message.destroy)


def click_add_button(username, task_entry, category, priority):  # add task to username's list
    try:
        with open(f"{username}.json", "r") as missions:
            missions = json.load(missions)
        if not isinstance(missions, list):  # check if missions is a list.
            missions = []  # Initializing an empty list
    except json.JSONDecodeError:
        missions = []
    task = task_entry.get().strip()
    category_of_task = category.get()
    if task and (category_of_task != "Select a category"):
        new_task = {"task": task, "category": category_of_task, "priority": priority}
        missions.append(new_task)
        with open(f"{username}.json", "w") as new:
            json.dump(missions, new)
        print(task)
        temporary_message(add_task_frame, f"{task} ({category_of_task}) succesfully added!", 11, 1)
        task_entry.delete(0, tk.END)
        category.set("Select a category")
    else:
        temporary_message(add_task_frame, "Please write a task or choose category.", 11, 1)


# photos
v = tk.PhotoImage(file="v-green.png")
square = tk.PhotoImage(file="square-outline-7.png")

# frames
add_task_frame = tk.Frame(root, bg="#DCDCDC")
opening_frame = tk.Frame(root, bg="#DCDCDC")
delete_all_frame = tk.Frame(root, bg="#DCDCDC")
going_frame = tk.Frame(root, bg="#DCDCDC")
show_frame = tk.Frame(root, bg="#DCDCDC")
delete_frame = tk.Frame(root, bg="#DCDCDC")
sign_up_frame = tk.Frame(root, bg="#DCDCDC")
sign_in_frame = tk.Frame(root, bg="#DCDCDC")
menu_frame = tk.Frame(root, bg="#DCDCDC")
en_del_frame = tk.Frame(root, bg="#DCDCDC")


def opening(username):  # displays the main menu and hides other frames
    add_task_frame.grid_forget()
    delete_all_frame.grid_forget()
    going_frame.grid_forget()
    show_frame.grid_forget()
    delete_frame.grid_forget()
    sign_in_frame.grid_forget()
    opening_frame.grid(row=0, column=0, padx=0, pady=0)

    opening_frame.grid_columnconfigure(0, weight=1)
    opening_frame.grid_columnconfigure(1, weight=1)
    opening_frame.grid_columnconfigure(2, weight=1)
    opening_frame.grid_columnconfigure(3, weight=1)

    label(opening_frame, "", 12).grid(row=0)
    label(opening_frame, "Welcome to my Task Manager!", 16).grid(columnspan=4, row=2, pady=20)
    label(opening_frame, "Choose option:", 12).grid(columnspan=4, row=3, pady=20)

    add_task_button = button(opening_frame, "Add Task", command=lambda: add_task(username))
    add_task_button.grid(column=2, pady=15, row=6)
    show_task_button = button(opening_frame, "Show Tasks", command=lambda: show_tasks(username))
    show_task_button.grid(column=2, pady=15, row=7)
    delete_task_button = button(opening_frame, "Delete Task", command=lambda: delete_task(username))
    delete_task_button.grid(column=2, pady=15, row=8)
    delete_all_tasks_button = button(opening_frame, "Delete All Tasks", command=lambda: delete_all_tasks(username))
    delete_all_tasks_button.grid(column=2, pady=15, row=9)


def add_task(username):  # displays the task addition screen and collects task details
    opening_frame.grid_forget()
    add_task_frame.grid(row=0, column=0, padx=0, pady=0)
    # Name of task
    label(add_task_frame, "Enter a new task:", 12).grid(row=3, column=0, pady=10)
    task_entry = tk.Entry(add_task_frame, width=50)
    task_entry.grid(row=3, column=1, padx=10)
    # category of task
    label(add_task_frame, "Category:",  12).grid(row=4, column=0)
    category = ttk.Combobox(add_task_frame, values=categories, state="readonly", font=("Arial", 12))
    category.grid(row=4, column=1, padx=10, pady=10)
    category.set("Select a category")
    # Priority level of task
    var = tk.StringVar(value="Low")
    options = ["Low", "Medium", "High"]
    label(add_task_frame, "Priority:", 12).grid(row=5, column=0)
    i = 5
    for option in options:
        choice = tk.Radiobutton(add_task_frame, text=option, bg="#DCDCDC", value=option, variable=var,
                                font=("Arial", 12))
        choice.grid(row=i, column=1)
        i += 1

    back_button = button(add_task_frame, "Back", command=lambda: opening(username))
    back_button.grid(row=8, column=0, pady=10, padx=10)
    add_task_button = button(add_task_frame, "Add Task", command=lambda: click_add_button(username, task_entry,
                                                                                          category, var.get()))
    add_task_button.grid(row=8, column=3, pady=50)


def all_tasks(username):  # deletes all tasks from the user's JSON file and displays a confirmation
    opening_frame.grid_forget()
    add_task_frame.grid_forget()
    delete_all_frame.grid_forget()
    going_frame.grid(row=0, column=0, padx=0, pady=0)

    try:
        with open(f"{username}.json", "r") as cleaning:
            missions = json.load(cleaning)
    except json.JSONDecodeError:
        missions = []

    for i in range(len(missions)-1, -1, -1):
        print("task deleted!")
        missions.pop(i)

    with open(f"{username}.json", "w") as clean:
        json.dump(missions, clean)

    image_label = tk.Label(going_frame, image=v, bg="#DCDCDC")
    image_label.grid(row=1, column=2, padx=10, pady=10)
    label(going_frame, "All the tasks deleted successfully!", 12).grid(row=2, column=2)
    label(going_frame, "", 12).grid(row=3)
    back_button = button(going_frame, "Back", command=lambda: opening(username))
    back_button.grid(row=10, column=1, pady=20, sticky="w")


def delete_all_tasks(username):  # the frame of delete all tasks
    opening_frame.grid_forget()
    going_frame.grid_forget()
    delete_all_frame.grid(row=0, column=0, padx=0, pady=0)

    label(delete_all_frame, "Are you sure you want to delete all the tasks?", 14).grid(row=1)
    no_button = button(delete_all_frame, "No", command=lambda: opening(username))
    no_button.grid(row=2, column=1, pady=10)
    yes_button = button(delete_all_frame, "Yes", command=lambda: all_tasks(username))
    yes_button.grid(row=2, column=2, pady=10, padx=10)


def show_tasks(username):  # show all the tasks of username
    opening_frame.grid_forget()
    show_frame.grid(row=0, column=0, padx=0, pady=0)

    for widget in show_frame.winfo_children():
        widget.destroy()

    category = ttk.Combobox(show_frame, values=categories, state="readonly", font=("Arial", 12))
    category.grid(row=0, column=1, padx=10, pady=10)
    category.set("Select a category")
    category_button = button(show_frame, "search", lambda: selected_category_for_showing_tasks(username,
                                                                                               category.get().strip()))
    category_button.grid(row=0, column=2, padx=10, pady=10)

    with open(f"{username}.json", "r") as data_of_user:
        missions = json.load(data_of_user)

    has = False
    i = 1
    for task in missions:
        has = True
        label(show_frame, "\u25A1", 24).grid(row=i, column=0)
        if task['priority'] == "Low":
            tk.Label(show_frame, text=f"{task['category']}- {task['priority']} - {task['task']}", fg="green", font=(12), bg="#DCDCDC").grid(row=i, column=1, pady=20)
        elif task['priority'] == "High":
            tk.Label(show_frame, text=f"{task['category']}- {task['priority']} - {task['task']}", fg="red", font=(12), bg="#DCDCDC").grid(row=i, column=1, pady=15)
        else:
            tk.Label(show_frame, text=f"{task['category']}- {task['priority']} - {task['task']}", fg="orange", font=(12), bg="#DCDCDC").grid(row=i, column=1, pady=15)
        i += 1
    if has==False:
        label(show_frame, "There are currently no tasks", 12).grid(row=i)
    back_button = button(show_frame, "Back", command=lambda :opening(username))
    back_button.grid(row=10, column=1, pady=20, sticky="w")


def selected_category_for_showing_tasks(username, selected_category):
    for widget in show_frame.winfo_children():
        if isinstance(widget, tk.Label) and widget.grid_info()['row'] > 0:
            widget.destroy()
    i = 1

    with open (f"{username}.json", "r") as data:
        missions=json.load(data)

    has=False
    for task in missions:
        if (task['category']==selected_category):
            has = True
            tk.Label(show_frame, image=square).grid(row=i, column=0)
            if task['priority'] == "Low":
                tk.Label(show_frame, text=f"{task['priority']} - {task['task']}", fg="green").grid(row=i, column=1)
            elif task['priority'] == "High":
                tk.Label(show_frame, text=f"{task['priority']} - {task['task']}", fg="red").grid(row=i, column=1)
            else:
                tk.Label(show_frame, text=f"{task['priority']} - {task['task']}", fg="orange").grid(row=i, column=1)
            i += 1

    if has==False:
        label(show_frame, "There are currently no tasks", 12).grid(row=i)


def del_tasl(missions, i, username):
    missions.pop(i)

    with open (f"{username}.json", "w") as file:
        json.dump(missions, file)
    delete_task(username)


def en_del_tasl(missions, i, username):  # frame of delete task
    delete_frame.grid_forget()
    en_del_frame.grid(row=0, column=0, padx=0, pady=0)
    label(en_del_frame,f"Are you sure you want delete {missions[i]['task']}?", 16).grid(row=1, column=1)
    yes_button= button(en_del_frame, "Yes", command=lambda: del_tasl(missions, i, username))
    yes_button.grid(row=2, column=2, pady=20, padx=20)
    no_button = button(en_del_frame, "No", command=lambda: delete_task(username))
    no_button.grid(row=2, column=1, pady=20, sticky="w")


def delete_task(username):  # delete task from username
    opening_frame.grid_forget()
    en_del_frame.grid_forget()
    delete_frame.grid(row=0, column=0, padx=0, pady=0)

    for widget in delete_frame.winfo_children():
        widget.destroy()

    try:
        with open(f"{username}.json", "r") as data:
            missions=json.load(data)
    except json.JSONDecodeError:
        missions=[]

    has=False
    i=1
    for task in missions:
        has=True
        x_button = tk.Button(delete_frame, text="\u274C",relief="flat",bg="#00796B",fg="white", command=lambda idx=i-1: en_del_tasl(missions, idx, username))
        x_button.grid(row=i, column=0, sticky="w")
        label(delete_frame,f"{task['category']} - {task['task']}",12).grid(row=i, column=1, padx=10)
        i+=1
    if has==False:
        label(delete_frame, "There are currently no tasks", 12).grid(row=1, column=1)
    back_button = button(delete_frame, "Back", command=lambda :opening(username))
    back_button.grid(row=10, column=1, pady=20, sticky="w")



def check_email(email):  # Check if the email is valid
    str = r'^[a-zA-Z0-9._-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'
    return re.match(str, email) is not None
def sumbit(username, password, email, name): #check the details and submit the details to json file
    new_data={"name":name, "email": email, "username":username, "password":password}
    i=0
    if new_data['name']=="":
        tk.Label(sign_up_frame, text="Name can't be empty", fg="red").grid(row=6+i, column=1)
        i+=1
    if new_data['email']=="":
        tk.Label(sign_up_frame, text="email can't be empty", fg="red"). grid(row=6+i, column=1)
        i+=1
    if new_data['username'] == "":
        tk.Label(sign_up_frame, text="Username can't be empty", fg="red").grid(row=6+i, column=1)
        i+=1
    if new_data['password']=="":
        tk.Label(sign_up_frame, text="Password can't be empty", fg="red").grid(row=6+i, column=1)
        i+=1
    if i>0:
        return
    valid=check_email(email)
    if valid==False:
        tk.Label(sign_up_frame, text="Invalid email!", fg="red").grid(row=6, column=1)
        return
    try:
        with open("users_data.json", "r") as users:
            data= json.load(users)
    except json.JSONDecodeError:
        data=[]

    for user in data:
        if user['username']==username:
            tk.Label(sign_up_frame, text="This username already taken!", fg="red").grid(row=6, column=1)
            return
        if user['email']==email:
            tk.Label(sign_up_frame,text="This email already taken!", fg="red").grid(row=6, column=1)
            return

    data.append(new_data)

    with open("users_data.json", "w") as users:
        json.dump(data, users, indent=4)

    with open(f"{username}.json", "w") as new:
        json.dump({},new)

    menu()


def sign_up(): #sign up frame
    opening_frame.grid_forget()
    menu_frame.grid_forget()
    sign_up_frame.grid(row=0, column=0, padx=0, pady=0)
    label(sign_up_frame, "Sign up Form:", 16).grid(row=0, column=0, padx=10, pady=15)

    for widget in sign_up_frame.winfo_children():
        widget.destroy()

    full_name=label(sign_up_frame, "Full name:", 12)
    full_name.grid(row=1, column=0, pady=10)
    full_name_entry=tk.Entry(sign_up_frame)
    full_name_entry.grid(row=1, column=1, pady=10)

    email=label(sign_up_frame, "Email:", 12)
    email.grid(row=2, column=0, pady=10)
    email_entry=tk.Entry(sign_up_frame)
    email_entry.grid(row=2, column=1, pady=10)

    username=label(sign_up_frame, "Username:", 12)
    username.grid(row=3, column=0, pady=10)
    username_entry=tk.Entry(sign_up_frame)
    username_entry.grid(row=3, column=1, pady=10)

    password=label(sign_up_frame, "Password", 12)
    password.grid(row=4, column=0, pady=10)
    password_entry=tk.Entry(sign_up_frame, show="*")
    password_entry.grid(row=4, column=1, pady=10)

    sumbit1 = button(sign_up_frame, "Submit", command=lambda: sumbit(username_entry.get().strip(), password_entry.get().strip(), email_entry.get().strip(), full_name_entry.get().strip()))
    sumbit1.grid(row=5, column=1, padx=15)

    back_button = button(sign_up_frame, "Back", menu)
    back_button.grid(row=5, column=0, pady=20, sticky="w")

def load_user(username, password): #check if there is username with this password
        try:
            with open(f"users_data.json", "r") as users_data:
                users=json.load(users_data)
        except json.JSONDecodeError:
                users=[]

        if users==[]:
            sign_in()

        for user in users:
            if user["username"]==username and user["password"]==password:
                opening(username)

        label(sign_in_frame, "The username or password are incorrect!", 12).grid(row=8, column=1)


def sign_in(): #sign in frame
    opening_frame.grid_forget()
    menu_frame.grid_forget()
    sign_in_frame.grid(row=0, column=0, padx=0, pady=0)
    username=label(sign_in_frame, "Username:", 12)
    username.grid(row=1, column=0)
    username_entry=tk.Entry(sign_in_frame)
    username_entry.grid(row=1, column=1)

    password=label(sign_in_frame, "Password", 12)
    password.grid(row=2, column=0)
    password_entry=tk.Entry(sign_in_frame, show="*")
    password_entry.grid(row=2, column=1)

    sumbit = button(sign_in_frame, "Sumbit", command=lambda: load_user(username_entry.get().strip(), password_entry.get().strip()))
    sumbit.grid(row=4, column=1, padx=15)

    back_button = button(sign_in_frame, "Back", menu)
    back_button.grid(row=4, column=0, pady=20, sticky="w")


def menu(): #first screen before get in
    opening_frame.grid_forget()
    sign_up_frame.grid_forget()
    sign_in_frame.grid_forget()
    menu_frame.grid(row=0, column=0, padx=0, pady=0)

    label(menu_frame, "Task Manager:", 16).grid(row=0, column=1, pady=15)
    up=button(menu_frame,"Sign up", command=sign_up)
    up.grid(row=1, column=1, pady=30)
    in_=button(menu_frame, "Sign in", command=sign_in)
    in_.grid(row=2, column=1)


menu()
root.mainloop()