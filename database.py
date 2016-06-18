class database:
    def __init__(self):
        #self.db = self.loadDB()
        self.db = dict()

    def lookUp(self, key):
        return self.db[key]

    def add (self, key, value):
        self.db[key] = value

    def delete(self, key):
        del self.db[key]

    def checkExist(self, key):
        return key in self.db

    def storeDB(self):
        pass

    def loadDB(self):
        pass
