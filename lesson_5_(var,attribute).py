class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    # First method
    def __str__(self):
        a = vars(self) # turn all variable into dict
        # print("a", a)
        
        s = ["{:10}: {}".format(k, v) for k, v in a.items()]
        return "\n".join(s)
        
    # Second method
    def __str__(self):
        attrs = ("fname", "lname", "age")
        s = ["{:10}: {}".format(a, getattr(self, a)) for a in attrs]
        return "\n".join(s)
        
     
if __name__ == '__main__':
    p = Person("Saksorn", "Ruangtanusak", 21)
    print(p)