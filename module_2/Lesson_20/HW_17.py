import math

#Task 1
class Animal:
    def talk(self):
        pass
    
class Cat(Animal):
    def talk(self):
        return 'meow'
    
class Dog(Animal):
    def talk(self):
        return 'woof woof'
    
def animal_talk(animal):
    return animal.talk()

cat = Cat()
dog = Dog()
print(animal_talk(cat))
print(animal_talk(dog))

#Task 2
class Library:
    def __init__(self, name, books = [], authors = []):
        self.name = name
        self.books = books
        self.authors = authors
        
    def new_book(self, name, year, author):
        if author not in self.authors:
            self.authors.append(author)
        book = Book(name, year, author)
        self.books.append(book)
        return book
    
    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]
    
    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors."
    
    def __repr__(self):
        return self.__str__()

class Book:
    book_amount = 0
    
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.book_amount += 1
    
    def __str__(self):
        return f'Book {self.name} was written by {self.author} in {self.year}.'
    
    def __repr__(self):
        return self.__str__()
    
class Author:
    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
    
    def __str__(self):
        return f'Author {self.name} was born in {self.country} on {self.birthday}.'
    
    def __repr__(self):
        return self.__str__()

author1 = Author("J.K. Rowling", "United Kingdom", "1965-07-31")
author2 = Author("George Orwell", "United Kingdom", "1903-06-25")

library = Library("City Library")
library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
library.new_book("1984", 1949, author2)

print(library)
print("Books by J.K. Rowling:", library.group_by_author(author1))
print("Books published in 1998:", library.group_by_year(1998))
print("Total books:", Book.book_amount)

#Task 3
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()
        
    def _simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("not Fraction object")
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("not Fraction object")
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("not Fraction object")
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("not Fraction object")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with a numerator of zero")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
    
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __repr__(self):
        return self.__str__()
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 + f2 == Fraction(3, 4))
print(f1 - f2 == Fraction(1, 4))
print(f1 * f2 == Fraction(1, 8))
print(f1 / f2 == Fraction(2, 1))

#Task 4
class Transport:
    def move(self):
        pass
    
class Car(Transport):
    def move(self):
        return 'Машина їде по дорозі'
    
class Boat(Transport):
    def move(self):
        return 'Човен пливе по воді'
    
def start_transport(transport):
    return transport.move()

car = Car()
boat = Boat()
print(start_transport(car))
print(start_transport(boat))

#Task 5
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def change_password(self, new_password):
        self.__password = new_password
        
    def check_password(self, input_password):
        return self.__password == input_password
    
    def __str__(self):
        return f'Username: {self.__username}'
    
user1 = User('Kate', '1234')
print(user1.check_password('1234'))
print(user1.check_password('4321'))
user1.change_password('4321')
print(user1.check_password('4321'))
print(user1)