

---

# Python Utility Functions and Classes

This repository contains a collection of Python utility functions and a class that perform a range of common tasks, including arithmetic operations, string manipulation, and basic object-oriented programming examples. This modular codebase is designed to be easy to understand and extend.

## Table of Contents

- [Functions](#functions)
  - [add_numbers](#add_numbers)
  - [is_even](#is_even)
  - [reverse_string](#reverse_string)
  - [count_vowels](#count_vowels)
  - [calculate_factorial](#calculate_factorial)
  - [apply_decorator](#apply_decorator)
  - [sort_by_age](#sort_by_age)
  - [merge_dicts](#merge_dicts)
- [Class](#class)
  - [Car](#car)
- [Installation](#installation)
- [Usage](#usage)

## Functions

### `add_numbers`

**Description:**  
Returns the sum of two numerical parameters.

**Usage:**

```python
result = add_numbers(20, 30)
print(result)  # Output: 50
```

### `is_even`

**Description:**  
Checks if a given number is even.

**Usage:**

```python
result = is_even(4)
print(result)  # Output: True

result = is_even(5)
print(result)  # Output: False
```

### `reverse_string`

**Description:**  
Returns the reversed version of the input string.

**Usage:**

```python
result = reverse_string("hello")
print(result)  # Output: "olleh"
```

### `count_vowels`

**Description:**  
Counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in a string, ignoring case.

**Usage:**

```python
result = count_vowels("memba")
print(result)  # Output: 2
```

### `calculate_factorial`

**Description:**  
Calculates the factorial of a non-negative integer.

**Usage:**

```python
result = calculate_factorial(4)
print(result)  # Output: 24
```

### `apply_decorator`

**Description:**  
Applies a decorator that prints "Decorator Applied" before executing the original function.

**Usage:**

```python
def sample_function():
    print("Function Executed")

decorated_function = apply_decorator(sample_function)
decorated_function()
# Output:
# Decorator Applied
# Function Executed
```

### `sort_by_age`

**Description:**  
Sorts a list of tuples (name, age) by age in ascending order.

**Usage:**

```python
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)
print(sorted_people)  # Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
```

### `merge_dicts`

**Description:**  
Merges two dictionaries. If there are common keys, their values are summed.

**Usage:**

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dicts(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 5, 'c': 4}
```

## Class

### `Car`

**Description:**  
Represents a Car object with attributes `make`, `model`, and `year`. Includes a method to display the car's details.

**Usage:**

```python
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
# Output: Car Information: 2020 Toyota Camry
```

## Installation

To use these utilities, clone the repository and run the code as needed in your Python scripts.

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YourRepository
   ```

3. (Optional) Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install any required dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can use the provided functions and class by importing them into your Python script. For example:

```python
from your_module import add_numbers, Car

# Using the add_numbers function
print(add_numbers(10, 5))  # Output: 15

# Using the Car class
car = Car("Honda", "Civic", 2022)
car.display_info()  # Output: Car Information: 2022 Honda Civic
```

Replace `your_module` with the actual name of the module file where the functions and class are defined.

---

Feel free to adjust the content as needed!