class Parent:
    def __init__(self,name):
        self.name=name

class Child(Parent):
    def __init__(self,childName,name):
        super().__init__(name)
        self.childName=childName

    def get_all_info(self):
        print(f"Parent name is {self.name} and the child name is {self.childName}")

child1=Child("ravi kant dubey","lal dubey")
child1.get_all_info()
