import tkinter as tk

root=tk.Tk() #create main window
root.title("Welcome!") # the name of the window in the bar
root.geometry("800x500") #define the size of window


welcome_frame=tk.Frame(root)
login_frame=tk.Frame(root)
signup_frame=tk.Frame(root)

def login():
    welcome_frame.grid_forget()
    signup_frame.grid_forget()
    login_frame.grid(row=0, column=0, padx=10, pady=10)

    root.title("Log In")
    tk.Label(login_frame, text="Login Form:", font=("Arial",16)).grid(row=0,column=0, padx=10, pady=5)

    tk.Label(login_frame, text="Username:", font=("Arial", 12)).grid(row=1,column=0, padx=10, pady=5)
    username_entry=tk.Entry(login_frame) #create field in order to write an input
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(login_frame, text="Password:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
    password_entry=tk.Entry(login_frame, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5)

    label = tk.Label(login_frame, text="", font=("Arial", 10))
    label.grid(row=5, column=0, columnspan=2, pady=5)
    def on_click_button():
        label.config(text="button clicked!")

    back_button=tk.Button(login_frame, text="Back",command=lambda:[show_welcome()])
    back_button.grid(row=4, column=1, pady=10)
    login_button=tk.Button(login_frame, text="Login", command= on_click_button)
    login_button.grid(row=4, column=2, padx=10, pady=10)

def signup():
    welcome_frame.grid_forget()
    login_frame.grid_forget()
    signup_frame.grid(row=0, column=0, padx=10, pady=10)

    root.title("Sign Up")
    tk.Label(signup_frame, text="Sign up Form:", font=("Arial",16)).grid(row=0,column=0, padx=10, pady=5)

    tk.Label(signup_frame, text="Full name:", font=("Arial", 12)).grid(row=1,column=0, padx=10, pady=5) #full name field
    name_entry=tk.Entry(signup_frame)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(signup_frame, text="Username:", font=("Arial", 12)).grid(row=2,column=0, padx=10, pady=5)
    username_entry=tk.Entry(signup_frame) #create field in order to write an input
    username_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(signup_frame, text="Password:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
    password_entry=tk.Entry(signup_frame, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(signup_frame, text="Confirm password:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5)
    password_entry_confirm=tk.Entry(signup_frame, show="*")
    password_entry_confirm.grid(row=4, column=1, padx=10, pady=5)

    label = tk.Label(signup_frame, text="", font=("Arial", 10))
    label.grid(row=5, column=0, columnspan=2, pady=5)
    def on_click_button():
        label.config(text="button clicked!")

    back_button=tk.Button(signup_frame, text="Back",command=lambda:[show_welcome()])
    back_button.grid(row=8, column=1, pady=10)
    signup_button=tk.Button(signup_frame, text="SignUp", command= on_click_button)
    signup_button.grid(row=8, column=2, padx=10, pady=10)


def on_enter(e):
    e.widget['bg']='lightblue'  # Change button color on hover

def on_leave(e):
    e.widget['bg']='blue'  # Reset button color when not hovered


def show_welcome():
    login_frame.grid_forget()
    signup_frame.grid_forget()
    welcome_frame.grid(row=0, column=0, padx=10, pady=10)

    global image
    image=tk.PhotoImage(file="welcome.png")
    tk.Label(welcome_frame, text="Welcome!", font=("Arial",16)).grid(row=0,column=0, padx=10, pady=5)
    image_label = tk.Label(welcome_frame, image=image)
    image_label.grid(row=1, column=0, padx=10, pady=10)


    login_button = tk.Button(welcome_frame, text="Login", font=("Arial", 14), bg="blue", fg="white", command=lambda: [login(), login_button.grid_forget(), signup_button.grid_forget()])
    login_button.grid(row=10, column=1, pady=5)
    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)

    signup_button = tk.Button(welcome_frame, text="Sign Up", font=("Arial", 14), bg="blue", fg="white",command=lambda: [signup(), login_button.grid_forget(), signup_button.grid_forget()])
    signup_button.grid(row=10, column=2, padx=10, pady=10)

show_welcome()
root.mainloop()



