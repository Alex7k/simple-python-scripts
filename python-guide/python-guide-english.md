# Python Learning Aid (MACHINE TRANSLATED)

- One line is executed after the other.
- Comments are written with a `#` at the beginning of the line. (They are ignored by Python)

---

## Data Types

There are different data types in Python:

- **Integer (Whole number)**

    ```python
    5
    ```

- **String (Text)**

    ```python
    "Hello World!"
    "123" # This is also a string because it is in "", even if it only contains numbers
    # You cannot do math with strings.
    ```

- **Float (Decimal number)**

    ```python
    3.14
    ```

- **Boolean (True or False)**

    ```python
    True
    False
    ```

---

## Converting Variables

Examples:

```python
int(x)   # Convert to integer (whole number)
str(x)   # Convert to string (text)
float(x) # Convert to float (decimal number)

age = "17" # String (text)
age_number = int(age) # Convert to integer (whole number)
```

---

## Assigning Variables

You can create variables and assign values to them. You can name them as you like, but it's good if the name relates to their content.

```python
a = 5 # Integer (whole number)
b = 10
name = "Alex" # String (text), must have "" or ''
```

### Calculating with Variables

Operators:

- `+`  Addition
- `-`  Subtraction
- `*`  Multiplication
- `/`  Division
- `%`  Modulo (remainder of division)

```python
c = a + b # c will be 15 because 5 + 10 = 15
c = a * b # c will be 50 because 5 * 10 = 50
a = a + 1 # a is increased by 1, so a = 6
```

Modulo operator returns the remainder of a division:

```python
10 % 2 # Returns 0. When you divide 10 by 2, the remainder is 0.
23 % 2 # Returns 1. 23 / 2 is 11 with remainder 1.
```

---

## Console Output/Input

```python
print("Hello World!") # Prints "Hello World!" to the console
```

### User input

```python
print("What is your name?: ")
name = input() # The user must enter something in the console, which is then stored in the variable 'name'
# Shortcut:
name = input("What is your name?: ")
```

---

## if-else (Conditions)

It first checks the condition of `if`. If the condition is true, the code block below is executed. If not, the next `elif` condition is checked, and if none of the conditions are true, the `else` block is executed.

You must always press Tab to indent.

```python
if a < b: # If a is less than b
    print("a is less than b")
elif a == b: # If a is equal to b
    print("a is equal to b")
else: # If none of the previous conditions apply
    print("a is greater than b")
```

---

## Loops

There are 2 types of loops: `for` and `while`

### for loop

Used for a specific number of iterations:

```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits: # 'fruit' is the temporary variable used for each element in the array 'fruits'
    print(fruit) # prints each value of the array (Apple, Banana, Cherry)
```

### while loop

Used as long as a condition is true:

```python
a = 0
b = 5
while a < b: # As long as a is less than b
    print("a is less than b")
    a = a + 1 # Increases a by 1 so the loop eventually ends, otherwise it would be an infinite loop
```

To make an infinite loop, you can write `while True:`.

---

## Getting Input from the User

```python
print("Please enter your name:")
name = input()
# DOES THE SAME AS:
name = input("Please enter your name:")
# Important: input() always returns a string! If you want to get a number (integer), do e.g.:
number = int(input("Enter a number: "))
```

---

## String Interpolation (Insert variables into strings/text)

There are 2 variants:

```python
print("Hello " + name + ", welcome!") # '+' joins strings
print(f"Hello {name}, welcome!") # You must add 'f' at the beginning to insert variables with {}
```

If the variable is a number, you must first convert it to a string:

```python
age = 17
print("I am " + str(age) + " years old.")
print(f"I am {age} years old.") # You must add 'f' at the beginning to insert variables with {}
```

---

## Arrays

Instead of just one variable with one value, you can define an array with a list of values:

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) # prints the first value of the array (Counting starts at 0) (Apple)
print(fruits[1]) # prints the second value of the array (Banana)

new_fruit = "Orange"
fruits.append(new_fruit) # Adds 'Orange' to the array 'fruits'
# ["Apple", "Banana", "Cherry", "Orange"]
```

Convert a string to an array (list):

```python
text = "Apple"
text_array = list(text)
# text_array -> ['A', 'p', 'p', 'l', 'e']
```

To do something, for example, 10 times:

```python
for i in range(10):
    print(i) # Prints the numbers from 0 to 9 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 'range(10)' would create an array with the values 0 to 9 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).
```

Count entries in an array:

```python
fruits = ["Apple", "Banana", "Cherry"]
number_of_fruits = len(fruits) # Returns the number of entries in the array 'fruits' (3 in this case)
```

---

## Modules

You can import modules to use additional functions.

Examples:

```python
import random
random_number = random.randint(1, 10) # Returns a random number between 1 and 10

fruits = ["Apple", "Banana", "Cherry"]
random_fruit = random.choice(fruits) # Returns a random fruit from the array 'fruits'
print(random_fruit) # "Cherry" or "Banana" or "Apple"
```

---

## Functions

You can create your own functions to encapsulate repeating logic and make the code clearer.

```python
def greeting(name): # Function with one parameter 'name'
    print(f"Hello {name}, welcome!") # Prints a greeting

name = input("What is your name?: ")
greeting(name) # Calls the function 'greeting' with the parameter 'name'

def sum_numbers(number_one, number_two): # Function with 2 parameters 'number_one' and 'number_two'
    return number_one + number_two # Returns the sum of number_one and number_two

a = 5
b = 10
result = sum_numbers(a, b) # a fills the parameter 'number_one' and b fills the parameter 'number_two'
print(f"The sum of {a} and {b} is {result}.") # Prints the sum of a and b
```

---

## My example solutions to some of the more difficult tasks

[https://github.com/Alex7k/simple-python-scripts/tree/main/python](https://github.com/Alex7k/simple-python-scripts/tree/main/python)
