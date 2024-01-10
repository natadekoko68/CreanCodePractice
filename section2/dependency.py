class B:
    def method_b(self):
        print("Class B method")

#Inheritance
class A_Inheritance(B):
    def method_a(self):
        super().method_b()

#Composition
class A_Composition:
    def __init__(self):
        self.b = B()

    def method_a(self):
        self.b.method_b()

a_inh = A_Inheritance()
a_comp = A_Composition()

a_inh.method_a()
a_comp.method_a()

