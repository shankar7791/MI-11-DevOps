from datetime import datetime , timedelta
date_1 = datetime(2012,12,2)
newdate = datetime.today() - date_1
print(newdate.days)