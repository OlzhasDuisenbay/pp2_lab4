"""Write a program using generator to print the even numbers between 0 and in comma
separated form where is input from console.n n"""
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("Enter a number:"))

print(",".join(even_generator(n)))
#5 >>> 0,2,4
