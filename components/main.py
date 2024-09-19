import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import os



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().title()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data={website:{"email":email,"password":password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please complete all empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
            file_path = os.path.join(documents_path, "my_pass.json")
            file_path2= os.path.join(documents_path, "my_pass.txt")
            with open(file_path2, "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                messagebox.showinfo(title="Password Copied",
                                    message=f"Password copied to the clipboard")
            try:
                with open(file_path,"r") as data_file:
                    old_data=json.load(data_file)
                    old_data.update(new_data)

                with open(file_path, "w") as data_file:
                    json.dump(old_data,data_file,indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
            except FileNotFoundError:
                with open(file_path, "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)

# ---------------------------- On Clicking Search Button------------------------------- #

def onclick_search_btn():
    documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
    file_path = os.path.join(documents_path, "my_pass.json")
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Type the website to search.")
    else:
        try:
            with open(file_path, "r") as data_file:
                old_data = json.load(data_file)
                for i in old_data:
                    if i==website:
                        messagebox.showinfo(title="Saved Credentials",message=f"Credentials for {website} are {old_data[i]}. Password copied to the clipboard")
                        pyperclip.copy(old_data[i]["password"])

        except FileNotFoundError:
            messagebox.showinfo(message=f"Credentials for {website} is not found. Please Add the password information first.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@example.com")
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

# Buttons
search_btn=Button(text="Search",width=15, command=onclick_search_btn)
search_btn.grid(row=1,column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)



#InfoButton
def show_info():
    messagebox.showinfo(title="About", message="MyPass is a Windows application for efficient password management. Simply enter your details and click \'Add\' button to store them safely in \'my_pass.txt file\' in the Documents folder.\n\nCreated By:Hari Ravendran")

btn=Button(text="info",font=("Arial",10,"italic"), command=show_info)
btn.grid(row=4,column=0)

window.mainloop()