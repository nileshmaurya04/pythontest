year=int(input("enter a year:"))
if (year % 100 == 0) and (year % 400 == 0):
    print("enter year()is a leap year".format(year))

elif (year % 4 == 0 and year % 100!=0):
 print("enter year()is a leap year".format(year))
else:
 print("enter year()is not a leap year".format(year))