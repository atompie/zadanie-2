import datetime

def get_id(list, mark):
    id = len(list.keys()) + 1
    if len(str(id)) <= 2:
        id = f"{mark}0{id}"
    return id

''' Vehicles'''
vehicles_registry = {}

class Vehicle():
    def __init__(self, vehicle_id, name, brand, tires, rims, vehicle_history):
        self.vehicle_id = vehicle_id
        self.name = name
        self.brand = brand
        self.tires = tires
        self.rims = rims
        self.vehicle_history = vehicle_history

    def add_history(self, vehicle_history, customer, period_of_time):
        number = len(self.vehicle_history.keys()) + 1
        vehicle_history[number] = [customer.customer_id, period_of_time]


def register_vehicle(registry, name, brand, tires, rims):
    vehicle_id = get_id(registry, "V")
    vehicle_history = {}
    registry[vehicle_id] = [name, brand, tires, rims, vehicle_history]
    return Vehicle(vehicle_id, name, brand, tires, rims, vehicle_history)

''' Customers '''
customers_registry = {}

class Customer():
    def __init__(self, customer_id, name, customer_history):
        self.customer_id = customer_id
        self.name = name
        self.customer_history = customer_history

    def add_history(self, customer_history, vehicle, period_of_time):
        number = len(self.customer_history.keys()) + 1
        customer_history[number] = [vehicle.vehicle_id, period_of_time]

def register_customer(registry, name):
    customer_id = get_id(registry, "C")
    customer_history = {}
    registry[customer_id] = [name, customer_history]
    return Customer(customer_id, name, customer_history)

''' Actions '''
def borrow(vehicle, customer):
    date = datetime.datetime.now()
    start = date.strftime("%d.%m.%y")
    if len(list(vehicle.vehicle_history.keys())) == 0:
        vehicle.add_history(vehicle.vehicle_history, customer, start)
        customer.add_history(customer.customer_history, vehicle, start)
    else:
        z = list(vehicle.vehicle_history.keys())[-1]
        w = vehicle.vehicle_history[z]
        if len(w) == 2:
            print("You can't borrow this vehicle")
        else:
            vehicle.add_history(vehicle.vehicle_history, customer, start)
            customer.add_history(customer.customer_history, vehicle, start)

def return_vehicle(vehicle, customer):
    date = datetime.datetime.now()
    end = date.strftime("%d.%m.%y")
    x = list(vehicle.vehicle_history.keys())[-1]
    y = vehicle.vehicle_history[x]
    start = y[1]
    vehicle.vehicle_history[x] = [customer.customer_id, start, end]
    customer.customer_history[x] = [vehicle.vehicle_id, start, end]

''' manual tests '''
car_1 = register_vehicle(vehicles_registry, 'car1', 'car', 'normal', 'norma;')
print(car_1.vehicle_id)

customer_1 = register_customer(customers_registry, 'customer1')
print(customer_1.customer_id)

borrow(car_1, customer_1)

print(car_1.vehicle_history)
print(customer_1.customer_history)

car_2 = register_vehicle(vehicles_registry, 'car2','car','red','rde')
print(car_2.vehicle_id)

return_vehicle(car_1, customer_1)
print(car_1.vehicle_history)

borrow(car_1, customer_1)
print(customer_1.customer_history)

customer2 = register_customer(customers_registry, 'customer2')
borrow(car_1, customer2)

print(customers_registry)
print(vehicles_registry)

print(car_1.vehicle_history)
