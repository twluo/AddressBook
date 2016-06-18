# -*- coding: utf-8 -*-
from database import database
from customer import customer

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


main()
