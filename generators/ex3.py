"""Define a function with a generator which can iterate the numbers,
which are divisible by 3 and 4, between a given range 0 and .n"""
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number:"))

print(list(divisible_by_3_and_4(n)))
#20 >>> [0, 12]
