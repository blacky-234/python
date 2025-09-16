class Father:

    def skill(self):
        print("Known gathering skill")
    

class Mother:
    def skill(self):
        print("Known cooking skill")

class Child(Mother,Father):  #TODO: Understand the concept
    
    def skill(self):
        super().skill()
        print("Know Painting skill")



c = Child()
c.skill()
print(Child.mro())