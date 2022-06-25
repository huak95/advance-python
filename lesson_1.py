# Create a simple class

class Player(object):
    def __init__(self): # dunder = __
        self.fname = ""
        self.lname = ""
        self.number= ""
    
class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number
        
    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname, self.lname, self.number)


if __name__ == '__main__':
    p1 = Player()
    p1.fname = "Loris"
    p1.lname = "Karius"
    p1.number = 1
    
    p2 = Player()
    p2.fname = "Alex"
    p2.lname = "Manninger"
    p2.number = 13
    
    p1a = Player2("Loris", "Karius", 1)
    p2a = Player2("Alex", "Manninger", 1)
    
    
    
    
    
        
    