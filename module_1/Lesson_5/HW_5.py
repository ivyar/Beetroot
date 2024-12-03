import random

# #Task 1
# random_num = random.randint(1, 10)
# user_num = int(input('Введіть число від 1 до 10: '))
# if random_num == user_num:
#     print('Вітаємо, ви вгадали!')
# else:
#     print(f'Введене число {user_num}, правильне число {random_num}\nВи програли!')

# #Task 2
# name = input("Введіть ім'я: ")
# age = int(input('Введіть вік: '))
# print(f"Hello {name}, on your next birthday you'll be {age + 1} years")

#Task 3
string = list(input('Your string: '))
for _ in range(5):
    random.shuffle(string)
    print(''.join(string))