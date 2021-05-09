#  write a function for convert age to days
from datetime import datetime
dd = int(input("Enter your Birth Date : "))
mm = int(input("Enter your Birth Month : "))
yy = int(input("Enter your Birth Year : "))
date = datetime(yy,mm,dd)
Days = datetime.today() - date
print(f"Total Days until today : {Days.days}")