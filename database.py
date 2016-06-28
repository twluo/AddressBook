import xml.etree.cElementTree as ET
import customer
class database:
    def __init__(self):
        #self.db = self.loadDB()
        self.db = dict()

    def lookUp(self, key):
        return self.db[key]

    def add(self, key, value):
        self.db[key] = value

    def delete(self, key):
        del self.db[key]

    def checkExist(self, key):
        return key in self.db

    def storeToXML(self):
        root = ET.Element("db")
        for key in self.db:
            customer = ET.SubElement(root, "customer")
            self.db[key].storeXML(customer)
        ET.ElementTree(root).write("db.xml")

    def loadFromXML(self):
        tree = ET.parse("db.xml")
        root = tree.getroot()
        for child in root:
            name = child[0].text
            phoneNumber = child[1].text
            address = child[2].text
            Customer = customer.customer(name, phoneNumber, address)
            self.add(phoneNumber, Customer)

