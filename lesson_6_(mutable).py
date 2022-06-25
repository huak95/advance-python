def immutable_demo():
    n = 4
    print("id(n) = {}, n={}".format(id(n), n))
    n += 1
    print("id(n) = {}, n={}".format(id(n), n))
    
    s = "Hello"
    print("id(s) = {}, s={}".format(id(s), s))
    s = s + "World"
    print("id(s) = {}, s={}".format(id(s), s))
    
def mutable_demo():
    #  สมบัติ
    #  เมื่อโดน a = b แล้วไปแก้ b ตัว a ก็จะเปลี่ยนด้วย
    
    n = [4]
    print("id(n) = {}, n={}".format(id(n), n))
    n[0] = n[0] + 1
    print("id(n) = {}, n={}".format(id(n), n))
    
    s = ["Hello"]
    print("id(s) = {}, s={}".format(id(s), s))
    s[0] = s[0] + "World"
    print("id(s) = {}, s={}".format(id(s), s))
    

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return "id(self) = {}, name = {}, phone = {}".format(id(self), self.name, self.phone)
        

if __name__ == "__main__":
        
    print("Immutable".center(20, "_"))
    immutable_demo()

    print()          
    print("Mutable".center(20, "_"))
    mutable_demo()
    
    

# OUTPUT 1
# _____Immutable______
# id(n) = 4347488656, n=4
# id(n) = 4347488688, n=5
# id(s) = 4348498800, s=Hello
# id(s) = 4350978352, s=HelloWorld

# ______Mutable_______
# id(n) = 4348528384, n=[4]
# id(n) = 4348528384, n=[5]
# id(s) = 4350977856, s=['Hello']
# id(s) = 4350977856, s=['HelloWorld']