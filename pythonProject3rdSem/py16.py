"""Program to take comma separated city names and print them in sorted order"""

city=str(input("Enter comma separated city names: "))
city_list=city.split(",")
sorted_city_list=sorted(city_list)
sorted_list=",".join(sorted_city_list)
print(sorted_list)