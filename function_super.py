class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello form Child!")


child = Child()
child.greet()