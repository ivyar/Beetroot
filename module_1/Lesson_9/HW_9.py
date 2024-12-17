#Task 1
from some_module import greeting

greeting()


#Task 2
from math import sqrt, sin, cos, pow

while True:
    temp = input('Введіть число або "q" для виходу з калькулятора: ')
    if temp == 'q':
        break
    else:
        try:
            num = int(temp)
            operation = input('Введіть бажану операцію з чотирьох доступних (sqrt, sin, cos, pow): ')
            if operation == 'sin':
                print(f'{operation}({num}) = {sin(num)}')
            elif operation == 'cos':
                print(f'{operation}({num}) = {cos(num)}')
            elif operation == 'pow':
                exp = int(input('Введіть степінь, до якого треба піднести число: '))
                print(f'{operation}({num}, {exp}) = {pow(num, exp)}')
            elif operation == 'sqrt':
                if num >= 0:
                    print(f'{operation}({num}) = {sqrt(num)}')
                else:
                    print(f'{operation}({num}) = {sqrt(-num)}i')
            else:
                print('Калькулятор не підтримує такої операції, спробуйте ще раз!')
        except ValueError:
            print('Ви ввели не число, спробуйте ще раз!')


#Task 3
from datetime import date
from calendar import month
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA')

current_date = date.today()

print('Поточний місяць:\n', month(current_date.year, current_date.month)) 
print('День тижня: ', current_date.strftime("%A"))


 


