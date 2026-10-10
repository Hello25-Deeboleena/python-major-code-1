#Program to take temperature in Fahrenheit from user and print it in Celsius. c = (f-32)*5/9

f=float(input("Enter temperature in fahrenheit: "))
c=(f-32)*5/9
b=round(c,2)
print(f"The temperature in celcius is {b}")
