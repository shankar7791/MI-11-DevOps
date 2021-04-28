def age_to_day(year,month,day):
    day=year*365+month*30+day
    return day
year,month,day = map(int, input("Enter age in yy/mm/dd formate ").split("/"))
print("Your total days on planet is : ", (age_to_day(year,month,day)))   