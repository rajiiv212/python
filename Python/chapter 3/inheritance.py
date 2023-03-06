from unicodedata import name


class person(object):
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name

    def isEmpl(self):
        return False

class empl(person):
    def isEmpl(self):
        return True
    
emp = person("greek1")
print(emp.getname(),emp.isEmpl())
emp = empl('greel2')
print(emp.getname(),emp.isEmpl())