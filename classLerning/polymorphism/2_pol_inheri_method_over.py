class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):  # override
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):  # override
        print("Penguin cannot fly")

for bird in (Sparrow(), Penguin(), Bird()):
    bird.fly()


p = Penguin()
p.fly()