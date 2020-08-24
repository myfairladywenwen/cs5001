import math
def main():
    angle = float(input("enter an angle in degrees: "))
    angle_in_r = math.radians(angle)
    cosine = math.cos(angle_in_r)
    sine = math.sin(angle_in_r)
    print("the cosine of", angle, "is",cosine)
    print("the sine of", angle, "is",sine)
main()
