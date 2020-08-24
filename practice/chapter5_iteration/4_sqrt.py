val = float(input('enter the number you want to get the sqrt:'))
if val < 0:
    print('invalid input, we will give you the sqrt of',-val)
    val = -val
result = 1
diff = result*result - val
while diff > 0.0000001 or diff < -0.00001:
    print(result, 'squared is', result*result)
    result = (result+val/result)/2
    diff = result*result - val
print('the sqrt of', val, 'is', result)

