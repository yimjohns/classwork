num = int(input("Enter the number for which you want to find the factorial > "))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of {} is {}".format(num, factorial(num)))
