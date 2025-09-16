class Student:
    def __init__(self, name, age):
        self.name = name        # public
        self._roll = 101        # protected (convention)
        self.__marks = 95       # private

    def show(self):
        print(f"Name: {self.name}, Roll: {self._roll}, Marks: {self.__marks}")

s = Student("Alice", 20)
print(s.name)      # ✅ Accessible
print(s._roll)     # ⚠️ Accessible, but should be treated as protected
# print(s.__marks) # ❌ AttributeError

s.show()           # ✅ Access through method

s._roll = 102
s.show()

print("Name-mangled",s._Student__marks)
s._Student__marks = 100
s.show()