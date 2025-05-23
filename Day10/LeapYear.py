def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True f"This is {leap_year}leap year"
    else:
        return False

leap_year = int(input("Enter Year:-\n"))

print(is_leap_year(leap_year))
