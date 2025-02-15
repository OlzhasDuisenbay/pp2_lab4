#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print(Today:",current_date.strftime("%Y-%m-%d"))
print("Tomorrow:",tomorrow.strftime("%Y-%m-%d"))
"""Yesterday: 2025-02-14
Today: 2025-02-15
Tomorrow: 2025-02-16"""
