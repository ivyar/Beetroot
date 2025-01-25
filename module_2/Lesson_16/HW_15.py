#Task 1
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
    def talk(self):
        return f'Hello, my name is {self.firstname} {self.lastname} and I am {self.age} years old'

person1 = Person('Carl', 'Johnson', 26)   
print(person1.talk())

#Task 2
class Dog:
    age_factor = 7
    
    def __init__(self, age):
        self.age = age
        
    def human_age(self):
        return self.age * Dog.age_factor
    
dog1 = Dog(3)
print(dog1.human_age())

#Task 3
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.channel = channels[0]
    
    def first_channel(self):
        self.channel = self.channels[0]
        return self.channel
    
    def last_channel(self):
        self.channel = self.channels[-1]
        return self.channel
    
    def turn_channel(self, N):
        self.channel = self.channels[N - 1]
        return self.channel
    
    def next_channel(self):
        if self.channel == self.channels[-1]:
            self.channel = self.channels[0]
        else:
            self.channel = self.channels[self.channels.index(self.channel) + 1]
        return self.channel
    
    def previous_channel(self):
        if self.channel == self.channels[0]:
            self.channel = self.channels[-1]
        else:
            self.channel = self.channels[self.channels.index(self.current_channel()) - 1]
        return self.channel
    
    def current_channel(self):
        return self.channel
    
    def exists(self, name):
        if type(name) == str and name in self.channels:
            return "Yes"
        elif type(name) == int and name <= len(self.channels):
            return "Yes"
        else:
            return "No"

controller = TVController(CHANNELS)
print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.exists(4) == "No")
print(controller.exists("BBC") == "Yes")

#Task 4
class Order:
    def __init__(self, order_id, items = {}, status = 'Нове'):
        self.order_id = order_id
        self.items = items
        self.status = status
        
    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price
        return self.items
    
    def calculate_total(self):
        return sum(self.items.values())
    
    def update_status(self, new_status):
        self.status = new_status
        return self.status
    
order = Order(1)
order.add_item("Товар 1", 100)
order.add_item("Товар 2", 200)
print(order.calculate_total())  # виведе: 300
order.update_status("в обробці")
print(order.status)  # виведе: в обробці

#Task 5
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        
    def promote(self, new_position):
        self.position = new_position
        return self.position
    
    def give_raise(self, amount):
        self.salary += amount
        return self.salary
    
    def get_info(self):
        return f'{self.name} - {self.position}, зарплата: {self.salary}'
    
employee = Employee("Марина", 1000, "Прибиральниця")
print(employee.get_info())
employee.promote("Адміністратор")
print(employee.get_info())
employee.give_raise(500)
print(employee.get_info())
