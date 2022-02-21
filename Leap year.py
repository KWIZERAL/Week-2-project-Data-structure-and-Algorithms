#Python program that checks whether a year is leap year or not

def checkYear(year):

    # Indicate true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
    
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

  #The Code
year = 2005
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")#Python program that checks whether a year is leap year or not

def checkYear(year):

    # Indicate true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
    
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

  #The Code
year = 2005
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")