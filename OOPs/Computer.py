class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def confug(self):
        print(self.cpu, self.ram)

    def compair(self,other):
        if self.ram == other.ram:
            return True
        else:
            return False


comp1 = Computer("i3", 13)
comp2 = Computer("i5", 13)
comp1.confug()


if comp1.compair(comp2):
    print("They are same")
else:
    print("They are not same")
