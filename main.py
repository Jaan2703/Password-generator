from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

window = Tk()
window.title("Password Manager")
window.minsize(width=700, height=500)
window.config(padx=50, pady=50)

# ............................Picture.....................................................
canva = Canvas(width=200, height=220)
lock_ing = PhotoImage(file="lock.png")
canva.create_image(102, 112, image=lock_ing)
canva.grid(column=1, row=0)

# .........................entry widget .....................................................
Website_entry = Entry(width=35)
Website_entry.grid(column=1, row=1, columnspan=2)
Website_entry.focus()
# "focus" will put the cursor in website entry widget so that the user dont want to put the cursor every time it open the project

Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2)
# Email_entry.insert(0,"jackmorde@gmail.com")
# if only one user is using the project then instead of putting same email id everytime use .insert method
# so that 1 email id will always will be in this entry widget

Password_entry = Entry(width=17)
Password_entry.grid(column=1, row=3)

# ...............................label widget...................................................
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)

Email_label = Label(text="Email/username:")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)


# ................................Password generator section......................................
# random module will take out tha values from below lists randomly adn then by using "shuffle" it  will shuffle those values
# and it will give one password after clicking generate password button
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(5, 7))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)

# "copy" will copy the password in the clipboard so that user can easily paste in website


# .....................................save password to a file..............................
# add method will insert all data in respective entry field. with the help of if statement it will check if any
# entry is empty or not and if it is empty it will show a pop up box otherwise it will save the data in file
def add():
    add_website = Website_entry.get()
    add_email = Email_entry.get()
    add_password = Password_entry.get()
    if len(add_website) == 0 or len(add_password) == 0 or len(add_password) == 0:
        messagebox.showinfo(title="oops", message="make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=add_website, message=f"These are the details \n email :{add_email}"
                                                                  f"\n Password:  {add_password} \n is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{add_website} | {add_email} | {add_password} \n")
                Website_entry.delete(0, END)
                Email_entry.delete(0, END)
                Password_entry.delete(0, END)


# "delete" will clear out all the data from three widgets after we click add button
# so that user can easiy use it for next time instead of deleting it everytime


Generate_password_button = Button(text="Generate password", command=generate_password)
Generate_password_button.grid(column=2, row=3)

Add_button = Button(text="Add", width=36, command=add)
Add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
