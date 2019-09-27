# Return formatted date of 3 days from now (no arguments)
from datetime import date, timedelta


def formatDate3Days():
    todaysDate = date.today()
    laterDate = todaysDate + timedelta(days=3)
    return (laterDate, todaysDate)
   
#print(todaysDate)
later, tDate = formatDate3Days()
print(later)
print(tDate)