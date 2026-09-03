 

import math

number = 25

print("Square root:", math.sqrt(number))


import random

number = random.randint(1, 10)

print("Random number:", number)



import datetime

today = datetime.date.today()

print("Today's date:", today)


import calendar

print("Calendar:")
print(calendar.month(2026, 8))


import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))

import os

print("Current directory:")
print(os.getcwd())



import time

print("Current time in seconds:")
print(time.time())


import sys

print("Python version:")
print(sys.version)



import json

student = {
    "name": "samruddhi",
    "age": 21
}

result = json.dumps(student)

print("JSON data:")
print(result)




from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

count = Counter(numbers)

print("Count of elements:")
print(count)