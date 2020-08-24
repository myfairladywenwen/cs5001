BASE = 32 # constants should be in ALL CAPS
CONVERSION_FACTOR = 5.0/9.0

f_temp = float(input('enter a temp in F:'))

c_temp = (f_temp - BASE) * CONVERSION_FACTOR

print("that is", round(c_temp, 2), "degrees in C")
