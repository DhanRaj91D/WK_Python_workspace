class Car:

    wheels = 4

    def __init__(self):
        self.mile = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mile = 8

print(c1.com, c1.mile, c1.wheels)
print(c2.com, c2.mile, c2.wheels)
