# 1.
# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle and Triangle.
# Implement methods to calculate area and perimeter for each shape.

import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Invalid radius. Enter a value > 0!")

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self.length = length
            self.width = width
        else:
            raise ValueError("Invalid values. Length and width should be greater than 0!")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        if l1 > 0 and l2 > 0 and l3 > 0:
            self.l1 = l1
            self.l2 = l2
            self.l3 = l3
        else:
            raise ValueError("Invalid values. They should be greater than 0!")

    def area(self):
        x = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(x * (x - self.l1) * (x - self.l2) * (x - self.l3))

    def perimeter(self):
        return self.l1 + self.l2 + self.l3


print("-----Ex 1-----")

circle = Circle(3)
print("Circle -> Area:", circle.area(), "-> Perimeter:", circle.perimeter())

rectangle = Rectangle(8, 3)
print("Rectangle -> Area:", rectangle.area(), "-> Perimeter:", rectangle.perimeter())

triangle = Triangle(2, 3, 4)
print("Triangle -> Area:", triangle.area(), "-> Perimeter:", triangle.perimeter())


# 2.
# Design a bank account system with a base class Account and subclasses
# SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal and interest calculation


class Account:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance can't be negative.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount} in account {self._account_number}. New balance: ${self._balance}.")
        else:
            print("Invalid amount. It should be greater than 0.")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid withdrawal. The amount should be greater than 0.")
        elif amount > self.get_balance():
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount} from account {self._account_number}. New balance: ${self._balance}.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.04):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, new_interest_rate):
        if 0 <= new_interest_rate <= 1:
            self._interest_rate = new_interest_rate
        else:
            print("Interest rate should be between 0 and 1.")

    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest of ${interest} added in account {self._account_number}. New balance: ${self._balance}.")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=50):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self._overdraft_limit

    def set_overdraft_limit(self, new_overdraft_limit):
        if new_overdraft_limit >= 0:
            self._overdraft_limit = new_overdraft_limit
        else:
            print("Overdraft limit can't be negative.")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid withdrawal. The amount should be greater than 0.")
        elif amount > self.get_balance() + self._overdraft_limit:
            print("Overdraft limit reached.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}.")


print("-----Ex 2-----")

savings_account = SavingsAccount(account_number="a1", balance=2500)
savings_account.withdraw(3000)
savings_account.withdraw(500)
savings_account.deposit(1000)
savings_account.calculate_interest()

checking_account = CheckingAccount(account_number="a2", balance=500, overdraft_limit=50)
checking_account.deposit(300)
checking_account.withdraw(700)
checking_account.withdraw(200)


# 3.
# Create a base class Vehicle with attributes like make, model and year,
# and then create subclasses for specific types of vehicles like
# Car, Motorcycle and Truck. Add methods to calculate mileage or
# towing capacity based on the vehicle type.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Make: {self.make} , Model: {self.model} , Year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, distance_traveled, fuel_consumed):
        super().__init__(make, model, year)
        self.distance_traveled = distance_traveled
        self.fuel_consumed = fuel_consumed

    def calculate_mileage(self):
        mileage = self.distance_traveled / self.fuel_consumed
        return mileage

    def __str__(self):
        return f"{super().__str__()}, Distance Traveled: {self.distance_traveled}, Fuel Consumed: {self.fuel_consumed}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, total_distance, total_time):
        super().__init__(make, model, year)
        self.total_distance = total_distance
        self.total_time = total_time

    def calculate_average_speed(self):
        average_speed = self.total_distance / self.total_time
        return average_speed

    def __str__(self):
        return f"{super().__str__()}, Total Distance: {self.total_distance}, Total Time: {self.total_time}"


class Truck(Vehicle):
    def __init__(self, make, model, year, load_weight):
        super().__init__(make, model, year)
        self.load_weight = load_weight

    def calculate_towing_capacity(self):
        towing_capacity = self.load_weight * 1.5
        return towing_capacity

    def __str__(self):
        return f"{super().__str__()}, Load Weight: {self.load_weight}"


print("-----Ex 3-----")

car = Car(make="car1", model="model1", year=2010, distance_traveled=234000, fuel_consumed=2340)
print(car)
mileage = car.calculate_mileage()
print(f"Mileage: {mileage}")

motorcycle = Motorcycle(make="motorcycle1", model="model2", year=2000, total_distance=50, total_time=110)
print(motorcycle)
average_speed = motorcycle.calculate_average_speed()
print(f"Average speed: {average_speed}")


truck = Truck(make="truck1", model="model3", year=2014, load_weight= 150)
print(truck)
towing_capacity = truck.calculate_towing_capacity()
print(f"Towing capacity: {towing_capacity}")

# 4.
# Build an employee hierarchy with a base class Employee. Create subclasses
# for different types of employees like
# Manager, Engineer and Salesperson
# Each subclass should have attributes like salary and methods related to their roles.


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name} , id: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, salary, team_size):
        super().__init__(name, id)
        self.salary = salary
        self.team_size = team_size

    def __str__(self):
        return f"{super().__str__()}, Position: Manager, Salary: {self.salary}, Team Size: {self.team_size}"

    def assign_task(self, employee_name, task):
        return f"{self.name} assigned a task to {employee_name.name} : {task}"


class Engineer(Employee):
    def __init__(self, name, id, salary, completed_tasks):
        super().__init__(name, id)
        self.salary = salary
        self.completed_tasks = completed_tasks

    def __str__(self):
        return f"{super().__str__()}, Position: Engineer, Salary: {self.salary}, Completed tasks: {self.completed_tasks}"

    def code(self):
        return f"{self.name} is coding."


class Salesperson(Employee):
    def __init__(self, name, id, salary, clients_served):
        super().__init__(name, id)
        self.salary = salary
        self.clients_served = clients_served

    def __str__(self):
        return f"{super().__str__()}, Position: Salesperson, Salary: {self.salary}, Clients served: {self.clients_served}"

    def make_sale(self):
        return f"{self.name} made a sale to one client."


print("-----Ex 4-----")


engineer = Engineer(name="Person2", id=2, salary=5000, completed_tasks=3)
print(engineer)
print(engineer.code())

salesperson = Salesperson(name="Person3", id=3, salary=4000, clients_served=200)
print(salesperson)
print(salesperson.make_sale())

manager = Manager(name="Person1", id=1, salary=10000, team_size=6)
print(manager)
print(manager.assign_task(engineer, "task1"))



# 5.
# Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird and Fish
# Add properties and methods to represent characteristics unique to each animal group.


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"


class Mammal(Animal):
    def __init__(self, name, color, legs_number):
        super().__init__(name, color)
        self.legs_number = legs_number

    def __str__(self):
        return f"{super().__str__()}, Type of animal: Mammal, Number of legs: {self.legs_number}"

    def eat(self, food):
        print(f"{self.name} is eating {food}.")


class Bird(Animal):
    def __init__(self, name, color, can_fly):
        super().__init__(name, color)
        self.can_fly = can_fly

    def __str__(self):
        return f"{super().__str__()}, Type of animal: Bird, Can fly?: {self.can_fly}"

    def fly(self):
        if self.can_fly == "yes":
            print(f"{self.name} has wings and can fly.")
        else:
            print(f"{self.name} cannot fly.")


class Fish(Animal):
    def __init__(self, name, color, is_carnivorous):
        super().__init__(name, color)
        self.is_carnivorous = is_carnivorous

    def __str__(self):
        return f"{super().__str__()}, Type of animal: Fish, Is carnivorous?: {self.is_carnivorous}"

    def swim(self):
        print(f"{self.name} is swimming.")


print("-----Ex 5-----")

monkey = Mammal("Monkey", "Brown", 2)
print(monkey)
monkey.eat("fruits")

pigeon = Bird("Pigeon", "Gray", "yes")
print(pigeon)
pigeon.fly()

salmon = Fish("Salmon", "Pink", "yes")
print(salmon)
salmon.swim()


# 6.
# Design a library catalog system with a base class LibraryItem and subclasses
# for different types of items like Book, DVD and Magazine
# Include methods to check out, return and display information about each item.


class LibraryItem:
    def __init__(self, item_name, item_id, is_checked_out=False):
        self.item_name = item_name
        self.item_id = item_id
        self.is_checked_out = is_checked_out

    def __str__(self):
        return f"Item name: {self.item_name}, Id: {self.item_id}, Checked Out: {self.is_checked_out}"

    def check_out(self):
        if self.is_checked_out:
            print(f"{self.item_name} is already checked out.")
        else:
            self.is_checked_out = True
            print(f"{self.item_name} checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.item_name} returned.")
        else:
            print(f"{self.item_name} is already in the library.")


class Book(LibraryItem):
    def __init__(self, item_name, item_id, author, is_checked_out=False):
        super().__init__(item_name, item_id, is_checked_out)
        self.author = author

    def __str__(self):
        return f"{super().__str__()}, , Type of item: Book, Author: {self.author}"

    def mark_as_read(self):
        print(f"{self.item_name} marked as read.")


class DVD(LibraryItem):
    def __init__(self, item_name, item_id, duration, is_checked_out=False):
        super().__init__(item_name, item_id, is_checked_out)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}, , Type of item: DVD, Duration: {self.duration}"

    def get_hours_duration(self):
        return self.duration / 60


class Magazine(LibraryItem):
    def __init__(self, item_name, item_id,  publication_date, is_checked_out=False):
        super().__init__(item_name, item_id, is_checked_out)
        self.publication_date = publication_date

    def __str__(self):
        return f"{super().__str__()}, , Type of item: Magazine, Publication date: {self.publication_date}"

    def get_publication_month(self):
        return self.publication_date.split("-")[1]


print("-----Ex 6-----")

book = Book(item_name="Book1", item_id=2, author="autor")
print(book)
book.mark_as_read()
book.check_out()

dvd = DVD(item_name="DVD1", item_id=121, duration=120)
print(dvd)
dvd.check_out()
dvd.return_item()
duration_hour = dvd.get_hours_duration()
print(f"Duration in hours: {duration_hour}")

magazine = Magazine(item_name="Magazine1", item_id=4, publication_date="2020-10-10")
print(magazine)
publication_month = magazine.get_publication_month()
print(f"Publication month: {publication_month}")
magazine.return_item()
magazine.check_out()
magazine.return_item()
