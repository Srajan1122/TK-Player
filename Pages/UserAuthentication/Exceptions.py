import tkinter as tk
from tkinter import messagebox
def Email_already_exists():
    messagebox.showerror('Error','The user with the provided \nemail already exists.')
def Phone_already_exists():
    messagebox.showerror('Error','The user with the provided \nphone number already exists.')
def User_not_Found():
    messagebox.showerror('Error','No user record found \nfor the given identifier.')
def Invalid_credentials():
    messagebox.showerror('Invalid Credentials','Please check your email \nor password.')




 