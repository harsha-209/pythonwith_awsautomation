
import os
import datetime

latest_time = datetime.datetime.now()

print(latest_time)
print(os.system('ls -lt| head -n2' ))
print(os.system('find . -type f -mmin -5'))
