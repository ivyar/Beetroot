import time

#Task 1
def logger(func):
    def wrapper(*args, **kwargs):
        if args:
            print(f'{func.__name__} called with {', '.join(map(str, args))}')
        else:
            print(f'{func.__name__} called with no arguments')
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(3, 4)

#Task 2
def stop_words(words: list):
    def decorator(func):
        def wrapper(name):
            sentence = func(name)
            for word in words:
                sentence = sentence.replace(word, '*')
            return sentence
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

#Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if not isinstance(name, type_):
                print('Неправильний тип аргументу')
                return False
            elif len(name) > max_length:
                print('Забагато символів')
                return False
            elif not any([word in name for word in contains]):
                print('Немає обов\'язкових символів')
                return False
            else:
                return func(name)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

#Task 1 from Slack
def timer(func):
    def wrapper(*ards, **kwargs):
        start = time.time()
        result = func(*ards, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start}')
        return result
    return wrapper

@timer
def sleep():
    time.sleep(2)
    
sleep()

#Task 2 from Slack
def is_int(func):
    def wrapper(*args, **kwargs):
        if all(map(lambda x: type(x) == int, args)):
            return func(*args, **kwargs)
        else:
            return 'Вхідні значення не цілі числа'
    return wrapper

@is_int
def add(x, y):
    return x + y

print(add(3, 4))
print(add(3.5, 4))
print(add('3', 4))
print(add('3', '4'))
