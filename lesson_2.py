class Player:
    def __init__(self, fname=None, lname=None, country=None):
        # Add = None ทำให้สามารถ pass input อะไรเข้าไปก็ได้
        self.fname = fname
        self.lname = lname
        self.country = country

    # add string method to print
    def __str__(self):
        return "fname: {}\nlname: {}\ncountry: {}".format(self.fname, self.lname, self.country)

if __name__ == '__main__':
    p1 = Player("Saksorn", "Ruangtanusak", "Thailand")
    print(p1.fname)
    print(p1.country)
    print(p1)
