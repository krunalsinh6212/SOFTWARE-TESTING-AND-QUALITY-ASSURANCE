# Main program

def isValid(age):
  if 18 <= age <= 60:
    return "Valid Age"
  else:
    return "Invalid Age"
  
# Define test cases

test_cases = [
  (18, "Valid Age"),  
  (17, "Invalid Age"),
  (19, "Valid Age"),
  (59, "Valid Age"), 
  (60, "Valid Age"), 
  (61, "Invalid Age")
]

# Run test cases

for i, (age, expected) in enumerate(test_cases):
  result = isValid(age)
  assert result == expected, f"Test case {i + 1} failed: age = {age}, expected = {expected}, result = {result}"
print("All test cases passed.")
