def evaluate(f, x, y):
    return f(x, y)

a = int(input('enter a number: '))
print(evaluate(lambda x, y: False if x == a else True, 2, 3))