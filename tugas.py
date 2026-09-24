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

percentage = float(input("Enter the percentage: "))
print(evaluate_performance(percentage))
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c