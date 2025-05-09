import datetime as dt

now=dt.datetime.now(tz='UTC')
year=now.year
print("Current date and time:", now)
print("Year:", year)
if now.year==2023:
    print("This year is 2023")
else:
    print("This year is not 2023")

week_day=now.weekday()
print("Day:", week_day)