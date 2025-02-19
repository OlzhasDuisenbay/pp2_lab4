#Create a generator that generates the squares of numbers up to some number .N
def square_generator(n):
    for i in range(n):
        yield round(i ** 2, n)

N = int(input())

for square in square_generator(N):
    print(square,end=" ")
# 5 >>> 0 1 4 9 16
