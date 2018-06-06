def leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        leap = True
    else:
        leap = False

    return leap

year = 2015
print("{0} = {1}".format(year,leap_year(year)))