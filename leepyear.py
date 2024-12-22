year = int(input("Enter a year: "))
if (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

elif (year % 400 == 0) and (year % 100 == 0):
    print(f'{year} is a leep year by using f string')

else:
    print("{0} is not a leap year".format(year))
    
    
# Another way to check leap year

def is_leap_year(year):
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)

print(is_leap_year(year))

# For checking leap year using list comprehension

leap_years = [year for year in range(1900, 2101) if is_leap_year(year)]
print(leap_years)

# For checking leap year using map function

leap_years = list(map(is_leap_year, range(1900, 2101)))
print(leap_years)

# For checking leap year using filter function

leap_years = list(filter(is_leap_year, range(1900, 2101)))
print(leap_years)


# for checking leap year using generator expression

leap_years = (year for year in range(1900, 2101) if is_leap_year(year))
print(list(leap_years))

