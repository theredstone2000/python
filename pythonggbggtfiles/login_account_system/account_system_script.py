import os
import json
from tkinter import messagebox, simpledialog
file = "data.json"
dir = input("data.json folder : ")
filepath = os.path.join(dir, file)
def manage_account(account_name):
    account_dict = {}
    #get the data
    with open(filepath, "r",encoding="utf-8") as f:
        account_dict = json.load(f)
    
    if account_dict[account_name].value("op_level") == "administrator" or account_dict[account_name].value("op_level") == "op": #checks if account is op or not
        dial = simpledialog.SimpleDialog(None, "what do you want to do ?", ["manage_other_accounts", "op_accounts", "deop_accounts","change_my_password","change_my_data","read_my_data", "logout"])
        do = dial.go()
        if do == 0: #if the answer is manage_otherè=_accounts
            dial = simpledialog.askstring(None,"type account name : ") #getting account name
            accounte = dial.go()
            try:
                account = account_dict[accounte]
            except:
                messagebox.showerror(message="this account does not exist !") #if the name has a typo
                return("redo")
            if not account["op_level"] == "normal": #to prevent modifying op accounts
                messagebox.showerror(message="you can't manage admin and op accounts !")
                return("redo")
            dial = simpledialog.SimpleDialog(None, "what do you want to do ?", ["ban","unban","reset_data"])
            setting = dial.go()
            if setting == 0 and account["banned"] == 0: #if the answer is ban
                account["banned"] = 1
            elif setting == 0 and account["banned"] == 1:
                messagebox.showerror(message="account is already banned !")
                return("redo")
            elif setting == 1 and account["banned"] == 1: #if the answer is unban
                account["banned"] = 0
            elif setting == 1 and account["banned"] == 0:
                messagebox.showerror(message="this account is not banned")
                return("redo")
            elif setting == 2: #answer = reset_data
                data = account["data"]
                data["secret_string"] = ""
                data["secret_list"] = []
                data["secret_dict"] = {}
                account["data"] = data
            account_dict[accounte] = account #registering the changes
            messagebox.showinfo(message="action succesfully performed !")
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            return("redo")
        elif do == 1 and account_dict[account_name].value("op_level") == "administrator": #answer = op_accounts
            dial = simpledialog.askstring(prompt="type the account's name : ")
            accounte = dial.go()
            try:
                account = account_dict[accounte]
            except:
                messagebox.showerror("this account does not exist !")
                return("redo")
            account["op_level"] = "op"
            account_dict[accounte] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(message="change succesfully registered")
        elif do == 1 and not account_dict[account_name].value("op_level") == "administrator":
            messagebox.showerror("only the admin can do that !")
            return("redo")
        elif do == 2 and account_dict[account_name].value("op_level") == "administrator": #answer = op_accounts
            dial = simpledialog.askstring(prompt="type the account's name : ")
            accounte = dial.go()
            try:
                account = account_dict[accounte]
            except:
                messagebox.showerror("this account does not exist !")
                return("redo")
            account["op_level"] = "normal"
            account_dict[accounte] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(message="change succesfully registered")
        elif do == 2 and not account_dict[account_name].value("op_level") == "administrator":
            messagebox.showerror("only the admin can do that !")
            return("redo")
        elif do == 3:
            current_password = simpledialog.askstring(prompt="Type your current password : ")
            current_hashed_password = hash(current_password)
            if not account_dict[account_name].value("hashed_password") == current_hashed_password:
                messagebox.showerror(None, "this is not your current password")
                return("redo")
            new_password = simpledialog.askstring(prompt="type your new password")
            new_password_2 = simpledialog.askstring(prompt="retype your new password : ")
            if not new_password == new_password_2:
                messagebox.showerror(message="the two passwords aren't the same")
                return("redo")
            new_hashed_password = hash(new_password)
            account = account_dict[account_name]
            account["hashed_password"] = new_hashed_password
            account_dict[account_name] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(message="change succesfully registered")
            return("redo")
        elif do == 4:
            account = account_dict[account_name]
            dial = simpledialog.SimpleDialog(None, "what data do you want to change", ["secret_string","secret_list","secret_dict"])
            setting = dial.go()
            if setting == 0:
                new_str = simpledialog.askstring(None, "type_new_string")
                account["secret_string"] = new_str
            elif setting == 1:
                dial = simpledialog.SimpleDialog(None, "what to do ?", ["add to end","change at index","remove at end"])
                settinge = dial.go()
                if settinge == 0:
                    new_value = simpledialog.askstring(None, "value : ")
                    account["secret_list"].append(new_value)
                elif settinge == 1:
                    index = simpledialog.askinteger(None, "Index : ")
                    value = simpledialog.askstring(None, "value : ")
                    account["secret_list"].pop(index)
                    account["secret_list"].insert(index,value)
                elif settinge == 2:
                    account["secret_list"].pop()
            elif setting == 2:
                dial = simpledialog.SimpleDialog(None, "what to do ?", ["add","change at key","remove at key"])
                settinge = dial.go()
                if settinge == 0:
                    new_value = simpledialog.askstring(None, "value : ")
                    new_key = simpledialog.askstring(None, "key : ")
                    account["secret_dict"] = account["secret_dict"] + {new_key: new_value}
                elif settinge == 1:
                    key = simpledialog.askstring(None, "Key : ")
                    value = simpledialog.askstring(None, "value : ")
                    account["secret_dict"].pop(key)
                    account["secret_dict"] = account["secret_dict"] + {key: value}
                elif settinge == 2:
                    key = simpledialog.askstring(None, "Key : ")
                    account["secret_dict"].pop(key)
            account_dict[account_name] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(None, "change succesfully registered")
            return("redo")
        elif do == 5:
            account = account_dict[account_name]
            dial = simpledialog.SimpleDialog(None, "what data to read ?", ["secret_string","secret_list","secret_dict"])
            setting = dial.go()
            if setting == 0:
                messagebox.showinfo(None, account["secret_string"])
            elif setting == 1:
                messagebox.showinfo(None, account["secret_list"])
            elif setting == 2:
                messagebox.showinfo(None, account["secret_dict"])
            return("redo")
        elif do == 6:
            return("logout")
    elif account_dict[account_name].value("op_level") == "normal": #checks if account is op or not
        dial = simpledialog.SimpleDialog(None, "what do you want to do ?", ["change_my_password","change_my_data","read_my_data", "logout"])
        do = dial.go()
        if do == 0:
            current_password = simpledialog.askstring(prompt="Type your current password : ")
            current_hashed_password = hash(current_password)
            if not account_dict[account_name].value("hashed_password") == current_hashed_password:
                messagebox.showerror(None, "this is not your current password")
                return("redo")
            new_password = simpledialog.askstring(prompt="type your new password")
            new_password_2 = simpledialog.askstring(prompt="retype your new password : ")
            if not new_password == new_password_2:
                messagebox.showerror(message="the two passwords aren't the same")
                return("redo")
            new_hashed_password = hash(new_password)
            account = account_dict[account_name]
            account["hashed_password"] = new_hashed_password
            account_dict[account_name] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(message="change succesfully registered")
            return("redo")
        elif do == 1:
            account = account_dict[account_name]
            dial = simpledialog.SimpleDialog(None, "what data do you want to change", ["secret_string","secret_list","secret_dict"])
            setting = dial.go()
            if setting == 0:
                new_str = simpledialog.askstring(None, "type_new_string")
                account["secret_string"] = new_str
            elif setting == 1:
                dial = simpledialog.SimpleDialog(None, "what to do ?", ["add to end","change at index","remove at end"])
                settinge = dial.go()
                if settinge == 0:
                    new_value = simpledialog.askstring(None, "value : ")
                    account["secret_list"].append(new_value)
                elif settinge == 1:
                    index = simpledialog.askinteger(None, "Index : ")
                    value = simpledialog.askstring(None, "value : ")
                    account["secret_list"].pop(index)
                    account["secret_list"].insert(index,value)
                elif settinge == 2:
                    account["secret_list"].pop()
            elif setting == 2:
                dial = simpledialog.SimpleDialog(None, "what to do ?", ["add","change at key","remove at key"])
                settinge = dial.go()
                if settinge == 0:
                    new_value = simpledialog.askstring(None, "value : ")
                    new_key = simpledialog.askstring(None, "key : ")
                    account["secret_dict"] = account["secret_dict"] + {new_key: new_value}
                elif settinge == 1:
                    key = simpledialog.askstring(None, "Key : ")
                    value = simpledialog.askstring(None, "value : ")
                    account["secret_dict"].pop(key)
                    account["secret_dict"] = account["secret_dict"] + {key: value}
                elif settinge == 2:
                    key = simpledialog.askstring(None, "Key : ")
                    account["secret_dict"].pop(key)
            account_dict[account_name] = account
            with open(filepath, "w", encoding="utf-8") as f:
                f = json.dump(account_dict)
            messagebox.showinfo(None, "change succesfully registered")
            return("redo")
        elif do == 2:
            account = account_dict[account_name]
            dial = simpledialog.SimpleDialog(None, "what data to read ?", ["secret_string","secret_list","secret_dict"])
            setting = dial.go()
            if setting == 0:
                messagebox.showinfo(None, account["secret_string"])
            elif setting == 1:
                messagebox.showinfo(None, account["secret_list"])
            elif setting == 2:
                messagebox.showinfo(None, account["secret_dict"])
            return("redo")
        elif do == 3:
            return("logout")
def login():
    with open(filepath, "r", encoding="utf-8") as f:
        account_dict = json.load(f)
    
    account_name = simpledialog.askstring(None, "username : ")
    password = simpledialog.askstring(None, "password : ")
    hashed_password = hash(password)
    if not hashed_password == account_dict[account_name].value("hashed_password"):
        messagebox.showerror(None, "your password or username was incorrect")
        quit(0)
    a = "redo"
    while a == "redo":
        a = manage_account(account_name)
    quit(1)
    
def register():
    with open(filepath, "r", encoding="utf-8") as f:
        account_dict = json.load(f)
    username = simpledialog.askstring(None, "username : ")
    password = simpledialog.askstring(None, "password : ")
    password2 = simpledialog.askstring(None, "retype password : ")
    if not password == password2:
        messagebox.showinfo(None, "passwords don't match !")
        quit(0)
    hashed_password = hash(password)
    account_dict = account_dict
    {username:{
        "op_level": "normal",
        "hashed_password": hashed_password,
        "data": {
            "secret_string": "",
            "secret_list": [],
            "secret_dict": {}
        }
    }}
    
    a = {}
    a.
    messagebox.showinfo(None, "successfully registered! \n now login !")
    login()





a = simpledialog.SimpleDialog(text="do you want to login, or register ?", buttons=["login","register"], master= None)
b = a.go()
if b == 0:
    login()
elif b == 1:
    register()





