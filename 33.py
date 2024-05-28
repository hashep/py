ask = [-7, -6, 3, 6, 7, 1]

print(list(filter(lambda x: x>0, ask)))
print(max(ask))
print(min(ask))

print(17/3)
print(round(17/3,4))

import time

print(time.strftime("%Y/%m/%d %H:%M:%S"))

import random
result = []
while len(result) <6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)

import datetime

sis = datetime.date(1885,12,31)
mi = datetime.date(2000,11,11)

print((mi-sis).days)
print((sis-mi).days)

import operator
data = [(윤
