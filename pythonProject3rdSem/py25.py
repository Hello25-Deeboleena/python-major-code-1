"""Program to calculate Simple Interest and Compound Interest. si = (p*r*t)/100 ; CI=
p*(1+r/100)^t"""

p=float(input("Enter price: "))
r=float(input("Enter rate: "))
t=int(input("Enter time: "))
simple_interest = (p * r * t) / 100
compound_interest= p*(1+r/100)**t
print(f"The simple interest is {simple_interest:.2f}")
print(f"The compound interest is {compound_interest:.2f}")