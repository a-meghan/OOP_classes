# Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    # Update the owner of vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner

# Create instances of Vehicle class and print
car_1 = Vehicle("ABC123", "car", "Aurora Doe")
car_2 = Vehicle("BCD234", "truck", "Reece Doe")
print("Original owners:")
print(car_1.owner)
print(car_2.owner)

# Update owner and print to show change
car_1.update_owner("Stella Mae")
car_2.update_owner("Odette Daniels")
print("\nUpdated owners:")
print(car_1.owner)
print(car_2.owner)