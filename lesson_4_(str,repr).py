class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):  # instance method
        return self.gold + self.silver + self.bronze
    
    # Setected __repr__ over __str__
    
    def __str__(self): # to Stings()
        return "{:15} g: {} s: {} b: {} t: {}"\
            .format(self.country, self.gold, self.silver, self.bronze, self.total())
            
    def __repr__(self): # string representation
        return "{}{}".format(self.__class__.__name__, repr((self.country, self.gold, self.silver, self.bronze)))
    
if __name__ == '__main__':
    
    # th = Medal("Thailand", 5, 6, 9)
    # print(th)
    # print(th.country,  "g", th.gold)
    
    m = [
        Medal("Thailand", 4, 5, 1),
        Medal("Japan", 14, 12, 1),
        Medal("USA", 20, 10, 4),
    ]
    
    for c in m:
        print(c)
        
    # Order
    # print(th) -> print(str(th))
    