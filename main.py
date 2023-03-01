import customtkinter, tkinter, subprocess
from tkinter import messagebox

def subproces():
    interface = interface_value.get()
    mac = input_field.get()
    commands = [f'ifconfig {interface} down', f'ifconfig {interface} hw ether {mac}', f'ifconfig {interface} up']
    for command in commands:
        subprocess.call(command, shell=True)
        print(command)
    input_field.delete(0, 'end')
    input_fieldTwo.delete(0, 'end')
    messagebox.showinfo("Success", "Mac address changed successfully!")

def on_entry_click(event):
    """Function to handle entry field click event and change color"""
    if input_field.get() == '00:11:22:33:44:55':
        input_field.delete(0, "end") # delete all the text in the entry field
        input_field.insert(0, '') #Insert blank for user input

    if input_fieldTwo.get() == 'wlan0':
        input_fieldTwo.delete(0, 'end')
        input_fieldTwo.insert(0, '')


def on_focusout(event):
    """Function to handle entry field focus out event and change color"""
    if input_field.get() == '':
        input_field.insert(0, '00:11:22:33:44:55')
    if input_fieldTwo.get() == '':
        input_fieldTwo.insert(0, 'wlan0')

app = customtkinter.CTk()
app.geometry('1040x640')
app.title('Mac Changer')

title = customtkinter.CTkLabel(app, text='this app will change your mac address ', font=('Roboto', 17))
title.grid(row=0, column=1, padx=290, pady=10, sticky="NW")

entryLabel = customtkinter.CTkLabel(app, text='New Mac: ', font=('Roboto', 15))
entryLabel.grid(row=1, column=0, padx=10, pady=10, sticky="E")

value = tkinter.StringVar()
input_field = customtkinter.CTkEntry(app, width=250, height=40, textvariable=value)
input_field.insert(0, '00:11:22:33:44:55')
# input_field.configure(fg='grey')
input_field.bind('<FocusIn>', on_entry_click)
input_field.bind('<FocusOut>', on_focusout)
input_field.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="W")

InterfaceLabel = customtkinter.CTkLabel(app, text='Interface Card: ', font=('Roboto', 15))
InterfaceLabel.grid(row=2, column=0, padx=10, pady=10, sticky="E")

interface_value = tkinter.StringVar()
input_fieldTwo = customtkinter.CTkEntry(app, width=250, height=40, textvariable=interface_value)
input_fieldTwo.insert(0, 'wlan0')
input_fieldTwo.bind('<FocusIn>', on_entry_click)
input_fieldTwo.bind('<FocusOut>', on_focusout)
input_fieldTwo.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="W")

submit = customtkinter.CTkButton(app, text="Change mac", command=subproces)
submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="W")

app.mainloop()
