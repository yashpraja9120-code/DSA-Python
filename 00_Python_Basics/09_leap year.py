# Write a function to check if the year number is a leap year.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter the year number: "))

if is_leap_year(year):
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")



