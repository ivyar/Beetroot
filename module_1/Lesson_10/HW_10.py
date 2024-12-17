#Task 1
def oops():
    raise IndexError

def function():
    try:
        oops()
    except IndexError:
        print('Є IndexError')
    except KeyError:
        print('Є KeyError')

function()

def oops():
    raise KeyError

function()


#Task 2
def func():
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        print(a ** 2 / b)
    except ValueError:
        print('Incorrect input, both values ​​must be numbers')
    except ZeroDivisionError:
        print('Incorrect input, the second number must be non-zero')

func()
