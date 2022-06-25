class Player:
    def __init__(self, fname, lname, country):
        self.fname = fname
        self.lname = lname
        self.country = country
        
    def __str__(self):
        return "fname: {}\nlname: {}\ncountry: {}".format(self.fname, self.lname, self.country)
    
if __name__ == '__main__':
    
    p1 = Player("Saksorn", "Ruangtanusak", "Thailand")
    print(p1.fname)
    print(p1.country)
    print(p1)
