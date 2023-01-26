from basics import *


def main():
    print("This program does some conversions between different units.")

    print("Conversion 2: Celsius to Fahrenheit.")
    c = float(input("Enter degrees in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c} degrees in celsius is {f} degrees in Fahrenheit.")

    print("Conversion 1: Fahrenheit to celsius.")
    f = float(input("Enter degrees in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f} degrees in Fahrenheit is {c} degrees in Celsius.")


main()
