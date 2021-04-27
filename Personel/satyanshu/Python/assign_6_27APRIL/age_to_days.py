def age_to_days(year,month,days):
    day=year*365+month*30+days
    return day
year,month,days = map(int, input("enter age in yy/mm/dd formate ").split("/"))
print("ur total days on this planet is : ", (age_to_days(year,month,days)))   
