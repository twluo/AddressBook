from customer import customer

class database:
    def __init__(self):
        #self.db = self.loadDB()
        self.db = dict()

    def lookUp(self, key):
        return self.db[key]

    def add (self, key, value):
        self.db[key] = value

    def checkExist(self, key):
        return key in self.db

    def storeDB(self):
        pass

    def loadDB(self):
        pass

flag = True
while flag:
    action = raw_input("What to do: ")
    if action == "exit":
        print "exiting"
        break
    name = raw_input("Enter Name: ")
    phoneNumber = raw_input("Enter Phone Number: " )
    address = raw_input("Enter Address: ")
    customer = customer(name, phoneNumber, address)
    print customer
