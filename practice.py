print("Welcome to your leap year checker")
year = int(input("Enter the year you want to check"))
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print(str(year) + "is a leap year")
        else:
            print("Not a leap year")
    else:
        print("Not a leap year")
else: 
    print("Not a leap year")