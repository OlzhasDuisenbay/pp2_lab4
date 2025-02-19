#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))

for num in countdown(n):
    print(num,end=" ")

#5 >>> 5 4 3 2 1 0
