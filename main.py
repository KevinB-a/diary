import calendar
from datetime import datetime

c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2020,2)
print(str)