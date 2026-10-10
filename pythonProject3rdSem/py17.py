"""Program to take comma separated city names and print only unique city names and in sorted
order."""
from enum import unique

city=str(input("Enter comma separated city names: "))
city_list=city.split(",")
unique_cities=set(city_list)
sorted_city_list=sorted(unique_cities)
sorted_list=",".join(sorted_city_list)
print(sorted_list)