from datetime import datetime , timedelta
date_1 = datetime(1998,2,1)
newdate = datetime.today() - date_1
print(newdate.days)