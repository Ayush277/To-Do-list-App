# adding python libraries like tkinter/messagebox/image import

import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# main window named app
app = tkinter.Tk()

# it includes Title of the app , size of the application , the application icon , background colour of the application
app.title("to do list ")
app.iconbitmap('TDL.ico')
app.geometry('450x550')
app.config(bg='#190482')

# font styles , with size and attributes of the font text.
font1 = ('consolas',20,'bold','underline')
font2 = ('Arial',13,'bold')
font3 = ('Speak pro',10,'bold')

# buttons images from directory
img_addtask = ImageTk.PhotoImage(Image.open('addt.png'))
img_deletetask = ImageTk.PhotoImage(Image.open('removet.png'))

# Function to add a task to the list and to set the priorities and warning .
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    if task:
        #task_list.insert(0,task)
        task_entry.delete(0 , END)
        task_list.insert(tkinter.END, f"{priority}: {task}")
        save_task()
    else:
       tkinter.messagebox.showwarning(title="WARNING", message="PLEASE ENTER A TASK")


# Function to delete a task to the list and warning.
def remove_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error', "choose a task.")



# application inview Title label , with font ,text colour, and bgcolour.

title_label = tkinter.Label(app,
    font=font1,bg='#190482',foreground='#FFA33C',
    text="TO DO LIST"
    )
title_label.place(x=135,y=1)

# adding priorities with dropbox button with x and y axis placement and also adding it to the function.

priorities = ["Low", "Medium", "High"]
priority_var = tkinter.StringVar(app)
priority_var.set(priorities[0])  # Default priority
priority_dropdown = tkinter.OptionMenu(app, priority_var, *priorities)
priority_dropdown.place(x=145,y=55)

# add button with different attributes

add_button = tkinter.Button(
    app,
    command=add_task,
    font=font2,
    text= "+ADD TASK ",
    cursor='hand1',
    width=40,
    image = img_addtask,
    height=40,
    bg='#E5E0FF')
add_button.place(x=25,y=55)

# remove button with different attributes

remove_button = tkinter.Button(
    app,
    command=remove_task,
    font=font2,
    text=" -REMOVE",
    cursor='hand2',
    width=40,
    image = img_deletetask,
    height=40)
remove_button.place(x=75,y=55)

#task entry box

task_entry = tkinter.Entry(
    app,
    font=font3,
    width=60)
task_entry.place(x=10,y=110)

# task list box

task_list= tkinter.Listbox(
    app,
    font=font3,
    height=20,
    width=60,
    selectmode=tkinter.SINGLE)
task_list.place(x=10,y=150)

# closing the main body tkinter code with the name of the application.
app.mainloop()


