from datetime import datetime, timedelta

now = datetime.now()
todat= datetime.today().date()
today = datetime.today()
tommorow = datetime.today() + timedelta(days=1)
print("Current date and time:", now)
print("Current date:", todat)
print("tommorow date:", tommorow)