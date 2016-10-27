# Автоматический вывод строки
import time
s = 'Wake up, Neo...\n'
for i in s:
	print(i, end='', flush = True)
	time.sleep(0.1)
"""
-------------------------------------------
import sys
print('This will be output immediately.')
sys.stdout.flush()

-------------------------------------------

print('This will be output immediately.', flush = True) #Python 3.5

-------------------------------------------
from sys import stdout
from time import sleep

for i in range(1,20):
    stdout.write("\r%d" % i)
    stdout.flush()
    sleep(1)
stdout.write("\r  \r\n") # clean up
"""
