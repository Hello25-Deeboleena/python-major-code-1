#Program to take 3 integers as input , print their max,min and mean

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
print(f"The maximum among the three is",max(a,b,c))
print(f"The min among the three is",min(a,b,c))
d=(a+b+c)/2
print(f"The mean among the three is",d)