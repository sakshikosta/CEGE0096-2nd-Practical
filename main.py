n = int (input("Provide the n-th number for the Fibonacci series: "))
a, b = 0, 1
while b < n:
    print(b)
    a, b = b, a + b