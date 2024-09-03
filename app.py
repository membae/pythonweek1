#add numbers
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(20,30))

#even function
def is_even(number):
    return number % 2 == 0
print(is_even(4))
#reverse string function
def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))
#count vowels function
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
print(count_vowels("memba"))
# calculate factorial function
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
print(calculate_factorial(4))
#apply decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator():
    print("decorator")

apply_decorator()

#sort list of tuple sequence
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)
print(sorted_people)
#merge dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add the key-value pair if key is only in the second dictionary
    
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dicts(dict1, dict2)
print(merged)
#OOP class creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()  
