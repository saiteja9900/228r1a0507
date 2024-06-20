class A:
    def method(self):
        print("A class is defined")
        # Removing super().method() because there's no superclass with method() in class A

class B:
    def method(self):
        print("B class is defined")
        # Removing super().method() because there's no superclass with method() in class B

class C(A, B):
    def method(self):
        print("C class is defined")
        super().method()  # This will call the method from the next class in the MRO (B in this case)

# Creating an instance of C and calling its method
obj = C()
obj.method()