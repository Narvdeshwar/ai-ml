class GrandFather:
    def __init__(self,g_name):
        self.g_name=g_name

class Father(GrandFather):
    def __init__(self,f_name):
        self.f_name=f_name

class Child(Father):
    def __init__(self,c_name,f_name,g_name):
        super().__init__(f_name)
        GrandFather.__init__(self,g_name)
        self.c_name=c_name

    def get_all_info(self):
        print(f"GrandFather name is {self.g_name}, Father name is {self.f_name} and the child name is {self.c_name}")

child1=Child("ravi kant dubey","lal dubey","Block dubey")
child1.get_all_info()
