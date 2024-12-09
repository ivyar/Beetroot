from functools import reduce 
from operator import sub, mul

#Task 1
def favorite_movie(name):
    print(f'My favorite movie is named {name}')
favorite_movie('Teenwolf')

#Task 2
def make_country(name, capital):
    country = {'name': name, 'capital': capital}
    print(country)
make_country('Ukraine', 'Kyiv')

#Task 3
def make_operation(operator, *args):
    if args:
        if operator == '+':
            return sum(args)
        elif operator == '-':
            return reduce(sub, args)
        elif operator == '*':
            return reduce(mul, args)
        else:
            print('Ви ввели неправильний оператор')
    else:
        return 0
print(make_operation('+', 7, 7, 2))