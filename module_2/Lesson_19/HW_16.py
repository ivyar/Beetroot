#Task 1
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def talk(self):
        return f'Привіт, мене звати {self.name} {self.surname} і мені {self.age} років.'
    
class Student(Person):
    def __init__(self, name, surname, age, university, faculty, course):
        super().__init__(name, surname, age)
        self.university = university
        self.faculty = faculty
        self.course = course
        
    def study(self):
        return f'Я вчуся у {self.university}, {self.faculty}, {self.course} курс.'

class Teacher(Person):
    def __init__(self, name, surname, age, university, faculty, position):
        super().__init__(name, surname, age)
        self.university = university
        self.faculty = faculty
        self.position = position
        
    def teach(self):
        return f'Я викладаю у {self.university}, {self.faculty}, {self.position}.'
    
person = Person('Марина', 'Дідур', 32)
print(person.talk())
student = Student('Оля', 'Костюк', 19, 'КПІ', 'Прикладна математика', 3)
print(student.study())
teacher = Teacher('Микола', 'Джонсонюк', 48, 'КПІ', 'Прикладна математика', 'Асистент')
print(teacher.teach())

#Task 2
class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]
    
    def remove_positives(self, nums):
        return [num for num in nums if num < 0]
    
    def filter_leaps(self, dates):
        return [date for date in dates if date % 4 == 0 and date % 100 != 0 or date % 400 == 0]

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

#Task 3
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        
class ProductStore:
    def __init__(self):
        self.products_amount = {}
        self.products_price = {}
        self.products_type = {}
        self.income = 0
        
    def add(self, product, amount):
        if product.name in self.products_amount.keys():
            self.products_amount[product.name] += amount
        else:
            self.products_amount[product.name] = amount
        self.products_price[product.name] = product.price * 1.3
        self.products_type[product.name] = product.type
        
    def set_discount(self, identifier, percent, identifier_type='name'):
        for name, price in self.products_price.items():
            if identifier_type == 'name' and name == identifier:
                self.products_price[name] = price * (1 - percent / 100)
            elif identifier_type == 'type' and self.products_type[name] == identifier:
                self.products_price[name] = price * (1 - percent / 100)
            else:
                return 'No products found'
            
    def sell_product(self, product_name, amount):
        if product_name in self.products_amount.keys() and self.products_amount[product_name] >= amount:
            self.products_amount[product_name] -= amount
            self.income += amount * self.products_price[product_name]
        else:
            raise ValueError('Not enough products in stock')
        
    def get_income(self):
        return self.income
    
    def get_all_products(self):
        return self.products_amount
    
    def get_product_info(self, product_name):
        if product_name in self.products_amount.keys():
            return product_name, self.products_amount[product_name]
        else:
            raise ValueError('Product not found')
        
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
print(s.get_all_products())
s.sell_product('Ramen', 10)
print(s.get_income())
assert s.get_product_info('Ramen') == ('Ramen', 290)

#Task 4
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        with open('module_2/Lesson_19/logs.txt', 'a') as file:
            file.write(msg + '\n')
            
try:
    raise CustomException("This is a custom error message.")
except CustomException as e:
    print(e)
    
#Task 5
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def get_info(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}'
    
class FullTimeEmployee(Employee):
    def __init__(self, name, position, salary, annual_bonus):
        super().__init__(name, position, salary)
        self.annual_bonus = annual_bonus
        
    def get_info(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Annual Bonus: {self.annual_bonus}'
    
class PartTimeEmployee(Employee):
    def __init__(self, name, position, hours_worked, hourly_rate):
        super().__init__(name, position, hours_worked * hourly_rate)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate
    
    def get_info(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hours Worked: {self.hours_worked}, Hourly Rate: {self.hourly_rate}'
    
full_time_employee = FullTimeEmployee('Ольга', 'Менеджер', 20000, 3000)
part_time_employee = PartTimeEmployee('Петро', 'Кур’єр', 200, 120)
print(full_time_employee.get_info())
print(part_time_employee.get_info())
print(part_time_employee.calculate_pay())

#Task 6
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
class Warehouse:
    def __init__(self, location, products = []):
        self.location = location
        self.products = products
        
    def add_product(self, product):
        self.products.append(product)
        return [product.name for product in self.products]
    
    def get_total_value(self):
        return sum([product.price * product.quantity for product in self.products])
    
product1 = Product('Молоко', 30, 10)
product2 = Product('Хліб', 10, 20)
product3 = Product('Сир', 100, 5)

warehouse = Warehouse('Київ')
print(warehouse.add_product(product1))
print(warehouse.add_product(product2))
print(warehouse.add_product(product3))
print(warehouse.get_total_value())
