# -*- coding: utf-8 -*-
from database import database
from customer import customer
import tkMessageBox
import Tkinter as tk

actionPrompt = "What to do: "
namePrompt = "Enter Name: "
phonePrompt = "Enter Phone Number "
addressPrompt = "Enter Address: "
invalidEntry = "Entry not found "
wishToAddPrompt = "Wish to enter new entry? "

def main():
    print "THIS IS MAIN"
    db = database()
    flag = True
    while flag:
        action = raw_input(actionPrompt)
        if action == "exit":
            break
        elif action == "new":
            phoneNumber = raw_input(phonePrompt)
            if not db.checkExist(phoneNumber):
                name = raw_input(namePrompt)
                address = raw_input(addressPrompt)
                db.add(phoneNumber, customer(name, phoneNumber, address))
            else:
                print db.lookUp(phoneNumber)
        elif action == "search":
            phoneNumber = raw_input(phonePrompt)
            if not db.checkExist(phoneNumber):
                print invalidEntry
                addNew = raw_input(wishToAddPrompt)
                if addNew == "yes" or addNew == "y":
                    name = raw_input(namePrompt)
                    address = raw_input(addressPrompt)
                    db.add(phoneNumber, customer(name, phoneNumber, address))
                else:
                    continue
            else:
                print db.lookUp(phoneNumber)
        elif action == "delete":
            phoneNumber = raw_input(phonePrompt)
            if not db.checkExist(phoneNumber):
                print invalidEntry
                continue
            else:
                db.delete(phoneNumber)
        elif action == "save":
            db.storeDBXML()
        elif action == "load":
            db.loadDBXML()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.PhoneNumberText = "Phone Number"
        self.NameText = "Name"
        self.AddressText = "Address"
        self.DeleteText = "Delete"
        self.AddText = "Add"
        self.SearchText = "Search"
        self.CancelText = "Cancel"
        self.DeletePrompt = "Are you sure you want to delete?"
        self.NotFoundPrompt = "Entry not found"
        self.UpdatePrompt = "Entry exists. Want to update?"
        self.db = database()
        self.db.loadFromXML()
        self.pack()
        self.createWidgets()
        master.protocol("WM_DELETE_WINDOW", self.exit)

    def exit(self):
        print "exiting"
        self.db.storeToXML()
        self.quit()

    def clear(self):
        self.PhoneEntry.delete(0, tk.END)
        self.NameEntry.delete(0, tk.END)
        self.AddressEntry.delete(1.0, tk.END)

    def delete(self):
        print "deleting"
        phoneQuery = self.PhoneEntry.get()
        if self.db.checkExist(phoneQuery):
            if tkMessageBox.askyesno(self.DeleteText, self.DeletePrompt):
                self.db.delete(phoneQuery)
                self.clear()
        else:
            tkMessageBox.showinfo(self.NotFoundPrompt, self.NotFoundPrompt)
            self.clear()

    def add(self):
        print "add"
        phoneQuery = self.PhoneEntry.get()
        name = self.NameEntry.get()
        address = self.AddressEntry.get(1.0, tk.END)
        if self.db.checkExist(phoneQuery):
            if tkMessageBox.askyesno(self.AddText, self.UpdatePrompt):
                self.db.add(phoneQuery, customer(name, phoneQuery, address))
            else:
                self.search()
        else:
            self.db.add(phoneQuery, customer(name, phoneQuery, address))

    def search(self):
        phoneQuery = self.PhoneEntry.get()
        if self.db.checkExist(phoneQuery):
            customer = self.db.lookUp(phoneQuery)
            self.clear()
            self.PhoneEntry.insert(0, customer.phoneNumber)
            self.NameEntry.insert(0, customer.name)
            self.AddressEntry.insert(1.0, customer.address)
        else:
            tkMessageBox.showinfo(self.NotFoundPrompt, self.NotFoundPrompt)
            self.clear()

    def createWidgets(self):
        self.PhoneLabel = tk.Label(self, text = self.PhoneNumberText)
        self.PhoneLabel.grid(row = 0, sticky = tk.W)
        self.PhoneEntry = tk.Entry(self, bd = 5)
        self.PhoneEntry.grid(row = 0, column = 1, columnspan = 2)
        self.NameLabel = tk.Label(self, text = self.NameText)
        self.NameLabel.grid(row = 1, sticky = tk.W)
        self.NameEntry = tk.Entry(self, bd = 5)
        self.NameEntry.grid(row = 1, column = 1, columnspan = 2)
        self.AddressLabel = tk.Label(self, text = self.AddressText)
        self.AddressLabel.grid(row = 2, sticky = tk.W)
        self.AddressEntry = tk.Text(self, bd = 5, width = 50, height = 4)
        self.AddressEntry.grid(row = 3, rowspan = 4, columnspan = 3)
        self.DeleteButton = tk.Button(self, text = self.DeleteText, command = self.delete)
        self.DeleteButton.grid(row = 7, sticky = tk.W)
        self.SearchButton = tk.Button(self, text = self.SearchText, command = self.search)
        self.SearchButton.grid(row = 7, column = 1, sticky = tk.W)
        self.AddButton = tk.Button(self, text = self.AddText, command = self.add)
        self.AddButton.grid(row = 7, column = 2, sticky = tk.E)

root = tk.Tk()
app = Application(master = root)
app.mainloop()
#main()
