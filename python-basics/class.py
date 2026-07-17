class Laptop:
    storage_type="ssd"
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
        print(f"Laptop has storage type {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.ram} RAM with {self.storage}GB {self.storage_type}")

l1=Laptop("16","512")
l2=Laptop("8","256")
l1.get_storage_type()
# l1.get_info()


######################################################
# Instance:
# 1. It has the first parameter `self`
# 2. It can access both the class and instance attributes

# Class
# 1. it has first parameter `cls`
# 2. it can only access the class attributes
# 3. it has decorators called as `@classmethod` so the class method can be accessed from the object
######################################################
