import datetime

t  = datetime.time(5,23,3)
print(t)
print(datetime.time.max)
print(datetime.time.min)
print(datetime.time.resolution)

today = datetime.date.today()
print(today)

print(today.timetuple())
print(today.day)

print(datetime.date.min)