"""Implement a generator called to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values.squares"""
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))


for square in squares(a, b):
    print(square,end=" ")

#4,8 >>> 16 25 36 49 64
