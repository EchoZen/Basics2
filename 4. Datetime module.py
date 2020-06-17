import datetime
# print(dir(datetime))
# print(help(datetime.date)) # Year, month, day
gvr= datetime.date(1956,1,31)
print(gvr) # Default format in python: yyyy-mm-dd

# Timedelta lets you add or subtract number of days
random_date= datetime.date(2000,1,1)
dt= datetime.timedelta(100) # 100 days
print(random_date+dt) # Adds 100 days to a date

# Specify date format
message= 'GVR was born on {:%A, %B %d, %Y}.' # which day of the week, month+day, year
print(message.format(gvr))

# datetime, date and time class
spacex_date = datetime.date(2017,3,30)
spacex_time = datetime.time(22,27,0) # Hours, min, second
spacex_datetime= datetime.datetime(2017,3,30,22,27,0)
print(spacex_date)
print(spacex_time) # hh:minmin:ss
print(spacex_datetime)

# print today's datetime
now= datetime.datetime.today()
print(now)
print(now.minute)

# String parse time, strptime()
# Converts string to datetime
moon_landing= '7/20/1969'
moon_landing_datetime= datetime.datetime.strptime(moon_landing, '%m/%d/%Y')
# write the format of moon_landing
print(moon_landing_datetime) # printed result is normal python format