# Пособие по изучению Python (МАШИННЫЙ ПЕРЕВОД)

* Каждая строка выполняется последовательно, одна за другой.
* Комментарии пишутся с `#` в начале строки. (Python их игнорирует)

---

## Типы данных

В Python есть разные типы данных:

* **Integer (целое число)**

  ```python
  5
  ```

* **String (строка, текст)**

  ```python
  "Hello World!"
  "123" # Это тоже строка, потому что она в "", даже если содержит только числа
  # Со строками нельзя выполнять математику.
  ```

* **Float (число с плавающей точкой, десятичное число)**

  ```python
  3.14
  ```

* **Boolean (логический тип: True или False)**

  ```python
  True
  False
  ```

---

## Преобразование типов

Примеры:

```python
int(x)   # Преобразовать в целое число (integer)
str(x)   # Преобразовать в строку (text)
float(x) # Преобразовать в число с плавающей точкой (decimal number)

age = "17" # Строка (text)
age_number = int(age) # Преобразовать в целое число (integer)
```

---

## Присваивание переменных

Вы можете создавать переменные и присваивать им значения. Называть их можно как угодно, но лучше, чтобы имя отражало содержимое.

```python
a = 5 # Integer (целое число)
b = 10
name = "Alex" # String (строка/текст), должна быть в "" или ''
```

### Вычисления с переменными

Операторы:

* `+`  Сложение
* `-`  Вычитание
* `*`  Умножение
* `/`  Деление
* `%`  Modulo (остаток от деления)

```python
c = a + b # c будет 15, потому что 5 + 10 = 15
c = a * b # c будет 50, потому что 5 * 10 = 50
a = a + 1 # a увеличивается на 1, значит a = 6
```

Оператор modulo возвращает остаток от деления:

```python
10 % 2 # Возвращает 0. При делении 10 на 2 остаток 0.
23 % 2 # Возвращает 1. 23 / 2 это 11 и остаток 1.
```

---

## Вывод/ввод в консоли

```python
print("Hello World!") # Печатает "Hello World!" в консоль
```

### Ввод пользователя

```python
print("What is your name?: ")
name = input() # Пользователь должен ввести что-то в консоли, это сохранится в переменную 'name'
# Сокращённо:
name = input("What is your name?: ")
```

---

## if-else (условия)

Сначала проверяется условие `if`. Если оно истинно, выполняется блок кода ниже. Если нет — проверяется следующее условие `elif`, и если ни одно условие не истинно, выполняется блок `else`.

Всегда нужно нажимать Tab для отступа (indentation).

```python
if a < b: # Если a меньше b
    print("a is less than b")
elif a == b: # Если a равно b
    print("a is equal to b")
else: # Если ни одно из предыдущих условий не подходит
    print("a is greater than b")
```

---

## Циклы

Есть 2 типа циклов: `for` и `while`

### Цикл for

Используется для заданного количества итераций:

```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits: # 'fruit' — временная переменная для каждого элемента массива 'fruits'
    print(fruit) # печатает каждое значение массива (Apple, Banana, Cherry)
```

### Цикл while

Используется, пока условие истинно:

```python
a = 0
b = 5
while a < b: # Пока a меньше b
    print("a is less than b")
    a = a + 1 # Увеличивает a на 1, чтобы цикл в итоге завершился, иначе он был бы бесконечным
```

Чтобы сделать бесконечный цикл, можно написать `while True:`.

---

## Получение ввода от пользователя

```python
print("Please enter your name:")
name = input()
# ДЕЛАЕТ ТО ЖЕ САМОЕ, ЧТО И:
name = input("Please enter your name:")
# Важно: input() всегда возвращает строку! Если хотите получить число (integer), сделайте, например:
number = int(input("Enter a number: "))
```

---

## Интерполяция строк (вставка переменных в строки/текст)

Есть 2 варианта:

```python
print("Hello " + name + ", welcome!") # '+' соединяет строки
print(f"Hello {name}, welcome!") # Нужно добавить 'f' в начале, чтобы вставлять переменные через {}
```

Если переменная — число, её сначала нужно преобразовать в строку:

```python
age = 17
print("I am " + str(age) + " years old.")
print(f"I am {age} years old.") # Нужно добавить 'f' в начале, чтобы вставлять переменные через {}
```

---

## Массивы

Вместо одной переменной с одним значением можно определить массив (список) значений:

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) # печатает первое значение массива (нумерация начинается с 0) (Apple)
print(fruits[1]) # печатает второе значение массива (Banana)

new_fruit = "Orange"
fruits.append(new_fruit) # Добавляет 'Orange' в массив 'fruits'
# ["Apple", "Banana", "Cherry", "Orange"]
```

Преобразование строки в массив (list):

```python
text = "Apple"
text_array = list(text)
# text_array -> ['A', 'p', 'p', 'l', 'e']
```

Сделать что-то, например, 10 раз:

```python
for i in range(10):
    print(i) # Печатает числа от 0 до 9 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 'range(10)' создаст массив со значениями от 0 до 9 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).
```

Подсчитать количество элементов в массиве:

```python
fruits = ["Apple", "Banana", "Cherry"]
number_of_fruits = len(fruits) # Возвращает количество элементов в массиве 'fruits' (в этом случае 3)
```

---

## Модули

Можно импортировать модули, чтобы использовать дополнительные функции.

Примеры:

```python
import random
random_number = random.randint(1, 10) # Возвращает случайное число между 1 и 10

fruits = ["Apple", "Banana", "Cherry"]
random_fruit = random.choice(fruits) # Возвращает случайный фрукт из массива 'fruits'
print(random_fruit) # "Cherry" или "Banana" или "Apple"
```

---

## Функции

Можно создавать собственные функции, чтобы выносить повторяющуюся логику и делать код понятнее.

```python
def greeting(name): # Функция с одним параметром 'name'
    print(f"Hello {name}, welcome!") # Печатает приветствие

name = input("What is your name?: ")
greeting(name) # Вызывает функцию 'greeting' с параметром 'name'

def sum_numbers(number_one, number_two): # Функция с 2 параметрами 'number_one' и 'number_two'
    return number_one + number_two # Возвращает сумму number_one и number_two

a = 5
b = 10
result = sum_numbers(a, b) # a подставляется в 'number_one', b — в 'number_two'
print(f"The sum of {a} and {b} is {result}.") # Печатает сумму a и b
```

---

## Мои примеры решений для некоторых более сложных задач

[https://github.com/Alex7k/simple-python-scripts/tree/main/python](https://github.com/Alex7k/simple-python-scripts/tree/main/python)
