class Parent:
    def feature(self):
        print("Parent feature")

class Child1(Parent):
    def child1_feature(self):
        print("Child1 feature")

class Child2(Parent):
    def child2_feature(self):
        print("Child2 feature")

c1 = Child1()
c1.feature()       # From Parent
c1.child1_feature()

c2 = Child2()
c2.feature()       # From Parent
c2.child2_feature()

print(Child1.mro())
print(Child2.mro())