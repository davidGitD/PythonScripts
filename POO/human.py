class human:
    def __init__(self,name,city):
        self.age = 0
        self.name = name
        self.city = city

    def getIdentity(self):
        print('Name:',self.name,'Age:',self.age,'City:',self.city)

    def birthday(self):
        self.age = self.age+1
        print("Happy birthday!! Now you are:",self.age)

#INHERITANCE
class Vampire(human):
    def __init__(self,blood,name,city):
        super().__init__(name,city)
        self.blood = blood
        
    def isVampire(self):
        if self.city == 'castellon' or self.blood == 0:
            print('He is a VAMPIREEEE')
        else:
            print('He is human')

bob = Vampire(1,'bob','castellon')
bob.isVampire()

hdavid = human('David','Castellon')
hjep = human('Jep','Barcelona')

#hdavid.getIdentity()
#hjep.getIdentity()
#hdavid.birthday()
