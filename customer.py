import xml.etree.cElementTree as ET

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

    def storeXML(self, root):
        ET.SubElement(root, "name").text = self.name
        ET.SubElement(root, "phoneNumber").text = self.phoneNumber
        ET.SubElement(root, "address").text = self.address

