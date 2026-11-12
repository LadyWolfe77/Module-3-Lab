#create super class
class Vehicle():
    def __init__(self, type):
        self.type = type
#create class with inheritance
class Automobile(Vehicle):
    def __init__(self,type, year, make, model, doors, roof):
        super().__init__(type)

        self.year = int(year)
        self.make = make
        self.model = model
        self.make = make 
        self.doors = doors
        self.roof = roof

#Accept input for car and store in vehicle super class
vehicle_type = input("What type of vehicle? ")

#Ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes
while True:
    year = input("What year? ")
    if year.isdigit() and 1886 <= int(year) <= 2027:
        year = int(year)
        break
    else:
        print("Invalid. Year must be between 1886 and 2027.")

make = input("What make? ")

model = input("What model? ")

while True:
    doors = input("2 or 4 doors? ")
    if doors in ("2","4"):
        doors = int(doors)
        break
    else:
        print("Enter a 2 or 4.")

while True:
    roof = input("Solid or sunroof? ")
    if roof in ("solid", "sunroof"):
        break
    else:
        print("Enter 'solid' or 'sunroof' ")

my_car = Automobile(vehicle_type, year, make, model, doors, roof)

#Output the data in an easy-to-read and understandable format
print("\n---Vehicle Information---")
print(f"Vehicle type: {my_car.type}")
print(f"Year: {my_car.year}")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Doors: {my_car.doors}")
print(f"Roof: {my_car.roof}")
