from datetime import datetime
x1=datetime.today()
x2=datetime.strptime("20 June 2022, 16:00:00", "%d %B %Y, %H:%M:%S")
c=(x1-x2).seconds
print(c)