#Task 1
def local_variable_count(func):
    return func.__code__.co_nlocals

def test():
    x = 10
    y = 20
    z = 30
    return x + y + z

print(local_variable_count(test))

#Task 2
def outer_function():
    def inner_function():
        return "Inside Inner Function"
    return inner_function

print(outer_function()())

#Task 3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

#Task 1 from Slack
def discount_10(price):
    return price * 0.9

def discount_20(price):
    return price * 0.8

def apply_discount(price, discount_func):
    return discount_func(price)

print(apply_discount(100, discount_10))
print(apply_discount(100, discount_20))

#Task 2 from Slack
def calculate_invoice(price_per_item, quantity):
    assert price_per_item > 0, "Ціна товару повинна бути більшою за 0"
    assert quantity > 0 and type(quantity) == int, "Кількість одиниць товару повинна бути цілим числом і більшою за 0"
    return price_per_item * quantity

print(calculate_invoice(10, 5))
# print(calculate_invoice(0, 5))
# print(calculate_invoice(10, 0))
# print(calculate_invoice(10, 5.5))
    