class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Player:
    def __init__(self,pid,name,age):
        self.pid =pid
        self.name =name
        self.age = age

    def __str__(self):
        return f"{self.pid} : {self.name}({self.age})"

    def myfunc(self):
        if self.pid > 10:
            self.pid = self.pid*4
            print(player)
        else:
            self.age = self.age*2
            print(player)



player = Player(12,"Francisco",25)


print(player.pid)
print(player.name)
print(player.age)

print(player)
player.myfunc()