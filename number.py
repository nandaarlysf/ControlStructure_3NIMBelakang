num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print(f"The largest number is: {find_largest(num1, num2, num3)}")
def print_odd_numbers(n):
  print(f"Odd numbers up to {n}:")
  for i in range(1, n + 1, 2):
    print(i, end=" ")
  print()
