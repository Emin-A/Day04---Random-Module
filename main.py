# Random Module
# random.randint(x, y)

# random whole numbers
import random
import my_module

random_integer = random.randint(0, 5)
print(random_integer)

print(my_module.pi)

# random float numbers from 0.0 to 1.0

random_float = random.random()
print(random_float)

# expand the range from 0.0 to 5.0
random_float * 5

# love score from previous exercise
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
