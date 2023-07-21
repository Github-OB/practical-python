# bounce.py
#
# Exercise 1.5

height = 100
bounce_constant = (3/5)
bounce_count = 0

while bounce_count < 10:
    height *= bounce_constant
    print(round(height, ndigits=4))
    bounce_count += 1



