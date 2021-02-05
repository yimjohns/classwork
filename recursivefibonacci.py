num = int(input("Enter the number for which to find fibonacci > "))

def fibonacci(n):
    if n == 0: 
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci (n - 2)
    
print("The fibonacci of {} is {}".format(num, fibonacci(num)))