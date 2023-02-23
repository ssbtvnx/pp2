import datetime
x=datetime.datetime.now()
y=x-datetime.timedelta(days=1)
t=x+datetime.timedelta(days=1)
print("yesterday",y)
print("today",x)
print("tomorrow",t)