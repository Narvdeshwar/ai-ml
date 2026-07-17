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

    @staticmethod
    def get_dicounted_price(price,discount_percentage):
        final_price=price-(price*discount_percentage/100)
        print(f"Final discounted price = {final_price}")

l1=Laptop("16","512")
l2=Laptop("8","256")
l1.get_storage_type()
# l1.get_info()
l1.get_dicounted_price(80_000,10)


######################################################
# Instance:
# 1. It has the first parameter `self`
# 2. It can access both the class and instance attributes

# Class
# 1. it has first parameter `cls`
# 2. it can only access the class attributes
# 3. it has decorators called as `@classmethod` so the class method can be accessed from the object

# static method
# 1. It doesn't have any `self` or `cls` parameter
# 2. It has decorators called as `@staticmethod`
######################################################
