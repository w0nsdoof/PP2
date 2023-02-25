from datetime import datetime , timedelta

# date1 = datetime(2019, 11 , 23)
# date2 = datetime(2019, 5, 3)

date1 = datetime(int(input("Year_1: ")), int(input("Month_1: ")), int(input("Day_1: ")))

date2 = datetime(int(input("Year_2: ")), int(input("Month_2: ")), int(input("Day_2: ")))

print((date1 - date2).total_seconds())