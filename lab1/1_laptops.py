class Laptop:
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram  # in GB


laptop1 = Laptop("Dell", "Inspiron", 16)
laptop2 = Laptop("HP", "Pavilion", 8)

print("Laptop 1:")
print("Brand:", laptop1.brand)
print("Model:", laptop1.model)
print("RAM (GB):", laptop1.ram)

print("\nLaptop 2:")
print("Brand:", laptop2.brand)
print("Model:", laptop2.model)
print("RAM (GB):", laptop2.ram)