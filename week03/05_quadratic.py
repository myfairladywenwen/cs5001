import math
def main():
    a = float(input("enter the coefficient of x squared: "))
    b = float(input("enter the coefficient of x: "))
    c = float(input("enter the constant: "))

    discriminant = b**2 - (4*a*c)
    root1 = ((-1*b)+ math.sqrt(discriminant)/(2*a))
    root2 = ((-1*b)- math.sqrt(discriminant)/(2*a))

    print("root1 = ", round(root1,3))
    print("root2 = ", round(root2,3))

main()