class Vehicle:
    def __init__(self, brand, model, year, price):

        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.price:.2f} лв."

    def __gt__(self, other):
        return self.price > other.price


if __name__ == "__main__":
    # Create several Vehicle objects
    car1 = Vehicle("Toyota", "Corolla", 2020, 28000)
    car2 = Vehicle("BMW", "X5", 2022, 95000)
    car3 = Vehicle("Tesla", "Model 3", 2023, 89000)

    # Print vehicle information
    print("🚘 Garage Vehicles:")
    print(car1)
    print(car2)
    print(car3)
    print("-" * 40)

    # Compare vehicles using the > operator
    if car2 > car1:
        print(f"{car2.brand} {car2.model} is more expensive than {car1.brand} {car1.model}.")
    else:
        print(f"{car1.brand} {car1.model} is more expensive than {car2.brand} {car2.model}.")

    if car3 > car2:
        print(f"{car3.brand} {car3.model} is more expensive than {car2.brand} {car2.model}.")
    else:
        print(f"{car2.brand} {car2.model} is more expensive than {car3.brand} {car3.model}.")