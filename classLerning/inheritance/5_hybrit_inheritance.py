class A:
    def featureA(self):
        print("Feature A")

class B(A):   # Single inheritance
    def featureB(self):
        print("Feature B")

class C(A):   # Hierarchical inheritance
    def featureC(self):
        print("Feature C")

class D(B, C):  # Multiple inheritance
    def featureD(self):
        print("Feature D")

d = D()
d.featureA()   # From A
d.featureB()   # From B
d.featureC()   # From C
d.featureD()   # From D

print(D.mro())
