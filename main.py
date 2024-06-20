from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    new_password = password_entry.get()

    if len(website) == 0 or len(new_password) == 0:
        messagebox.showwarning('Blank Field!', "Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(f'{website}', f'Here are the details entered \nUsername: {username} '
                                                     f'\nPassword: {new_password} \nIs it okay to save?')

        if is_ok:
            with open('pw_data.txt', mode='a') as file:
                file.write(f'{website} | {username} | {new_password}\n')
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
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2, sticky='w')
username_entry.insert(0, 'salami.tomie@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons for screen
generate_button = Button(text='Generate Password', highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
