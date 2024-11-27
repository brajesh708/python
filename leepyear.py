year = int(input("Enter a year: "))
if (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

elif (year % 400 == 0) and (year % 100 == 0):
    print(f'{year} is a leep year by using f string')

else:
    print("{0} is not a leap year".format(year))
