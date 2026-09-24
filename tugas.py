def evaluate_performance(percentage):
  if percentage >= 90:
    return "Excellent performance"
  elif percentage >= 80:
    return "Very Good performance"
  elif percentage >= 70:
    return "Good performance"
  elif percentage >= 60:
    return "Average performance"
  else:
    return "Needs Improvement (Below Average)"


# Example usage:
percentage = float(input("Enter student percentage: "))
print(evaluate_performance(percentage))
def find_largest(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c


# Example usage:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print(f"The largest number is: {find_largest(num1, num2, num3)}")
def print_odd_numbers(n):
  print(f"Odd numbers up to {n}:")
  for i in range(1, n + 1, 2):
    print(i, end=" ")
  print()


# Example usage:
n = int(input("Enter the limit n: "))
print_odd_numbers(n)
def print_design(n):
  for i in range(1, n + 1):
    for j in range(i):
      print(i, end=" ")
    print()


# Example usage:
n = int(input("Enter n value (e.g., 5): "))
print_design(n)