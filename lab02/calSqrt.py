import math
def main():
    x1 = float(input("Enter the first value for the first point: "))
    y1 = float(input("Enter the second value for the first point: "))
    x2 = float(input("Enter the first value for the second point: "))
    y2 = float(input("Enter the second value for the second point: "))
    result = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    print("the Euclidean distance between the two points is", result)   
main() 