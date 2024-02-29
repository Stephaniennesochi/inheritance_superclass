class digital_product:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        
    def display_info(self):
        print(f"Model is {self.model}")
        print(f"Brand is {self.brand}")
        
class laptop(digital_product):
    def __init__(self, model, brand, durability):
        
        super().__init__(model, brand)
        self.durability = durability
        
    def display_info(self):
        pass
        
object = laptop("Itel","P36","lasts long")
print(f"Model is {object.model}")
print(f"Brand is {object.brand}")
print(f"durability is that it {object.durability}")

object.display_info()