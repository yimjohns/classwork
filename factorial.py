num = int(input("Enter the number for which to find the factorial > "))
factorial = 1

for i in range(num, 0, -1):
    print(i, end=" ")
    factorial *= i

print("\nThe factorial of {} is {}".format(num, factorial))
