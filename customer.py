class customer:
    def __init__(self, name, phoneNumber, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address

    def __str__(self):
        string = "Name: " + self.name + "\n"
        string += "Phone Number: " + self.phoneNumber + "\n"
        string += "Address: " + self.address
        return string
