# --- Leap Year Finder --- #
while True:
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Sorry, that is not a valid year.")
        continue
    else:
        break
    
if (year < 1582):
    print("Sorry, {} pre-dates the Gregorian calendar.".format(year))

# --- The Triangle of Doom --- #  
else:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year!".format(year))
            else:
                print("{} is a common year!".format(year))
        else:
            print("{} is a leap year!".format(year))
    else:
        print("{} is a common year!".format(year))