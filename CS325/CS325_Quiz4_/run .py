from module1.areaOfCircle import calculateAreaOfCircle
from module2.numberToExponet import calculateNumberToExponet
from module3.factorial import calculateFactorial

def main():
    result1 = calculateAreaOfCircle(999)
    result2 = calculateNumberToExponet(9,12)
    result3 = calculateFactorial(111)

    print("Area of a circle with radius 999:",result1)
    print("9 to the 12 is:",result2)
    print("factorial of 111:",result2)

if __name__ == "__main__":
    main()