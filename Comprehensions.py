squared_list = []
squared_dict = dict()
numbers_set = set()
switched_numbers = dict()

def comprehension1():
    return [x**2 for x in range(10) if x % 2 == 0]

def comprehension2():
    return {x:x**2 for x in range(10) if x % 2 == 1}

def comprehension3():
    return {int(character) for character in "JWxdVL8hE8VRmU8vCUX8Y32tFmgn7hfm" if character.isdigit()}

def comprehension4():
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    return dict([(value, key) for key, value in numbers.items()])

def even_generator(num):
    if num % 2 != 0:
        i= num+1
    else:
        i = num
    while True:
        yield i
        i += 2

squared_list=comprehension1()
print(squared_list)
squared_dict=comprehension2()
print(squared_dict)
numbers_set=comprehension3()
print(numbers_set)
switched_numbers=comprehension4()
print(switched_numbers)
my_gen = even_generator(10)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
my_gen = even_generator(-3)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))