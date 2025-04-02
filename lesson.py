import time
from collections import deque
from array import array

class Lesson:
    def __init__(self):
        pass

    def introduction(self):
        print("\nProgramming is the process of writing instructions for computers to follow.")
        print("Python is a great first language because it's simple and powerful! Try typing:")
        print("print('Hello, World!')\n")
        input("Press Enter to continue...\n")

    def variables(self):
        print("\nVariables store data. Example:")
        print("name = 'Alice'\nage = 25\nprint(name, age)")
        print("Data types: Strings, Integers, Floats, Booleans")
        input("Try it and press Enter to continue...\n")

    def conditionals(self):
        print("\nConditional statements control decision-making.")
        print("Example:")
        print("x = 10\nif x > 5:\n    print('x is greater than 5')\nelse:\n    print('x is 5 or less')")
        input("Try it and press Enter to continue...\n")

    def loops(self):
        print("\nLoops help in repeating tasks.")
        print("Example:\nfor i in range(5):\n    print('Hello', i)")
        input("Try it and press Enter to continue...\n")

    def functions(self):
        print("\nFunctions help reuse code.")
        print("Example:\ndef greet():\n    print('Hello!')\ngreet()")
        input("Try it and press Enter to continue...\n")

    def lists_dictionaries(self):
        print("\nLists & Dictionaries store multiple values.")
        print("Example:\nfruits = ['Apple', 'Banana', 'Cherry']\nprint(fruits[0])")
        print("Dictionary Example:\nperson = {'name': 'Alice', 'age': 25}\nprint(person['name'])")
        input("Try it and press Enter to continue...\n")

    def data_structures(self):
        print("\nData Structures help organize and store data efficiently.")
        print("\nArrays (Fixed-size list of elements):")
        print("numbers = array('i', [1, 2, 3, 4, 5])\nprint(numbers[0])")
        print("\nStack (LIFO - Last In First Out):")
        print("stack = []\nstack.append(1)\nstack.append(2)\nstack.pop() # Removes 2")
        print("\nQueue (FIFO - First In First Out):")
        print("queue = deque([1, 2, 3])\nqueue.popleft() # Removes 1")
        print("\nLinked List (Node-based structure):")
        print("class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None")
        input("Press Enter to continue...\n")

    def mini_projects(self):
        print("\nMini Project: Create a simple calculator.")
        print("Try writing a Python program that asks for two numbers and an operation (+, -, *, /).\nThen perform the calculation.")
        input("Press Enter when you're ready to code it!\n")
