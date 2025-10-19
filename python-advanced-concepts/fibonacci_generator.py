def fibonacci(limit):

    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for num in fibonacci(20):
    print(num, end=" ")
