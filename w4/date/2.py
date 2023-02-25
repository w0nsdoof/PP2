from datetime import datetime , timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("", yesterday.strftime("%d.%m.%Y" ) , '\n', today.strftime("%d.%m.%Y") + " today" , '\n' , tomorrow.strftime("%d.%m.%Y") )