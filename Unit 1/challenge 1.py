def factorial(n):
  if n == 0:  # base case: factorial of 0 is 1
    return 1
  else:
    return n * factorial(
        n - 1)  # recursive case: multiply n with factorial of (n-1)


# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
