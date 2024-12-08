#Task 1
sentence = input('Введіть речення: ')
words = sentence.split()
count = {word : words.count(word) for word in words}
print(count)

#Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
price_of_the_stock = {item : stock[item] * prices[item] for item in stock.keys()}
print(price_of_the_stock)
print(sum(price_of_the_stock.values()))

#Task 3
list_with_tuples = [(i, i ** 2) for i in range(1, 11)]
print(list_with_tuples)

#Task 4
days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_dict = {i+1 : days_list[i] for i in range(len(days_list))}
days_dict_rev = {day : days_list.index(day)+1 for day in days_list} #інший спосіб ітерування як варіант
print(days_dict)
print(days_dict_rev)