
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def Fibonacci(n):
    if n < 0:
        print("Number should be greater that zero")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)	


print(Fibonacci(1))
#Result: 1
print(Fibonacci(6))
#Result: 8
print(Fibonacci(9))
#Result: 34
