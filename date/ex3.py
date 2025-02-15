#Write a Python program to drop microseconds from datetime.
from datetime import datetime

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", current_datetime_without_microseconds)

#Datetime without microseconds: 2025-02-15 15:06:43
