import time 
from calendar import isleap

localtime = time.localtime(time.time())
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)