import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_DIR)
import datetime

dat = datetime.datetime(1990,1,1)
b = (2018,1,2)
c = b[0]

print(c)
d = [[]]*3
print(d)
d[0]=10
print(d)
d[1].append(11)

print(d)