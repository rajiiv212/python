class Base1(object):
    def __init__(self) -> None:
        self.str1 = "greek1"
        print("Base1")

class Base2(object):
    def __init__(self) -> None:
        self.str2 = "greek2"
        print("Base2")

class Derived(Base1,Base2):
    def __init__(self):

        Base1.__init__(self)
        Base2.__init__(self)
        print("Derivend")

    def printstr(self):
        print(self.str1,self.str2)

ob = Derived()
ob.printstr()