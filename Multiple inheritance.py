class A:
    def method_a(self):
        print("This is method A")

class B:
    def method_b(self):
        print("This is method B")

class C(A, B):
    def method_c(self):
        print("This is method C")

# create an instance of C and call its methods
obj_c = C()
obj_c.method_a()  
obj_c.method_b()  
obj_c.method_c()  
