import math

# 1a) Create a function which takes a string and concatenates
# "@gmail.com" to this string before returning it # 1b) call and print this function on your name

def emailer(word):
    return word + "@gmail.com"

my_email = "ufoma"
output = emailer(my_email)
print(output)


# 2a) Fix the function below. It should take in a radius and calculate
# the area of a circle (pi * radius ^ 2)
import math
def areaCirc(rad):
    return math.pi * (rad ** 2)


# 2b) use this function to calc the area of a circle with a radius of 5
# (answer should be ~78.5398)
my_circle = 5
output = areaCirc(my_circle)
print(output)


# 3a) Create a function that converts kilometers to miles
# there are roughly 1.61 km in one mile
import math
def kilo_convert(kilos):
    return kilos * 0.62137119
    

# 3b) use this function to convert 10km to miles
kilometers = 10
output = kilo_convert(kilometers)
print(output)
