class Wallet:
    def __init__(self):
        self.amount = 0
        
    def earn(self, a):
        self.amount += a
        
    def spend(self, a):
        self.amount -= a
        
    def __str__(self):
        return "amount = {}".format(self.amount)
    
if __name__ == "__main__":
    
    dad = Wallet()
    dad.earn(100)
    print("dad's wallet", dad)
    
    mom = dad
    print(mom is dad)
    print("mom's wallet", mom)

    mom.spend(20)
    print("dad's wallet", dad)
    print("mom's wallet", mom)
    print(id(dad), id(mom))
    
    kid = Wallet()
    kid.earn(500)