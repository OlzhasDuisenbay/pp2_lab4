#Write a Python program to calculate two date difference in seconds
from datetime import datetime

date1 = datetime(2024, 2, 15, 12, 0, 0)
date2 = datetime(2024, 2, 18, 9, 30, 0)

difference_seconds = (date2 - date1).total_seconds()

print("Difference between the two dates in seconds:", difference_seconds)

#Difference between the two dates in seconds: 250200.0
