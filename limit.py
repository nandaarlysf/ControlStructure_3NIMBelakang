n = int(input("Enter the limit n: "))
print_odd_numbers(n)
def print_design(n):
  for i in range(1, n + 1):
    for j in range(i):
      print(i, end=" ")
    print()
