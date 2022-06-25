# dunder -> double underscore

class Alpha:
    normal = 1
    _lucky = 13
    __secret = 777
    
    def fx(self):
        print
    
if __name__ == '__main__':
    print(Alpha.normal)
    print(Alpha._lucky)
    # print(Alpha.__secret) # -> this will error
    print(Alpha._Alpha__secret)
    
    print(Alpha.__dict__) # --> show all attributes
    
    Alpha.normal = 99
    Alpha._lucky = 123
    Alpha.__secret = 9999

    print(Alpha.normal)
    print(Alpha._lucky)
    print(Alpha.__secret)
    print(Alpha._Alpha__secret)
    
#   Results
    # 99
    # 123
    # 9999
    # 777
    