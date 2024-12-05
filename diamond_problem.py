class A:
    def method(self):
        print("Method from A")


class B(A):
    pass


class C(A):
    pass


class D(C, B):
    pass


obj = D()
obj.method()
# print(D.__mro__)
