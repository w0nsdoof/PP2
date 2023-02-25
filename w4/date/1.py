from datetime import datetime, timedelta

# Отнять 5 дней от нынешней даты

current = datetime.today()

result = current - timedelta(days=5)

print(result.strftime("%d.%m.%Y"))

