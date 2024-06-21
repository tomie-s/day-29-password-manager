from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()

    try:
        with open('pw_data.json', mode='r') as file:
            file_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found.")
    else:
        if website in file_data:
            username = file_data[website]['username']
            password = file_data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {username} \nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f"No details saved for {website}.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    username = username_entry.get()
    new_password = password_entry.get()

    new_data = {
        website: {
            'username': username,
            'password': new_password
        }
    }

    # save data file that contains new info
    def file_write(new_file):
        with open('pw_data.json', mode='w') as data_file:
            json.dump(new_file, data_file, indent=4)

    if len(website) == 0 or len(new_password) == 0:
        messagebox.showwarning('Blank Field!', "Please don't leave any field empty")
    else:
        try:
            with open('pw_data.json', mode='r') as file:
                # open and read the data file
                file_data = json.load(file)
        except FileNotFoundError:
            file_write(new_data)
        else:
            # update data file with new info
            file_data.update(new_data)
            file_write(file_data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels for screen
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Text inputs
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky='w')
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2, sticky='w')
username_entry.insert(0, 'salami.tomie@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons for screen
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
