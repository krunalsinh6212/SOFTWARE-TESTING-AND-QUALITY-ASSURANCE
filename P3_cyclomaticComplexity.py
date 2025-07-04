import re

# Step 1: Date Validation Function
def is_valid_date(d, m, y):
    if 1900 <= y <= 2100:
        if 1 <= m <= 12:
            if 1 <= d <= 31:
                if (m in [4, 6, 9, 11]) and d > 30:
                    return False
                elif m == 2:
                    leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
                    if (leap and d > 29) or (not leap and d > 28):
                        return False
                return True
    return False

# Step 2: Test Cases to Cover Independent Paths
test_cases = [
    (15, 3, 2020),    # Valid date
    (31, 4, 2021),    # April 31 → Invalid
    (30, 4, 2021),    # April 30 → Valid
    (29, 2, 2020),    # Leap year Feb 29 → Valid
    (30, 2, 2020),    # Leap year Feb 30 → Invalid
    (29, 2, 2021),    # Non-leap year Feb 29 → Invalid
    (15, 10, 1800),   # Invalid year
]

# Step 3: Execute Test Cases
print("Date\t\tValid?")
for d, m, y in test_cases:
    result = is_valid_date(d, m, y)
    print(f"{d:02d}-{m:02d}-{y} \t{'✅ Valid' if result else '❌ Invalid'}")


# Step 4: Cyclomatic Complexity Estimator
def estimate_cyclomatic_complexity(code: str) -> int:
    # Basic decision keywords
    decision_keywords = [r'\bif\b', r'\belif\b', r'\bfor\b', r'\bwhile\b',
                         r'\bcase\b', r'\bcatch\b', r'&&', r'\|\|']

    complexity = 1  # Start at 1
    for keyword in decision_keywords:
        matches = re.findall(keyword, code)
        complexity += len(matches)

    return complexity

# Step 5: Date Code as String
date_code = """
def is_valid_date(d, m, y):
    if 1900 <= y <= 2100:
        if 1 <= m <= 12:
            if 1 <= d <= 31:
                if (m in [4, 6, 9, 11]) and d > 30:
                    return False
                elif m == 2:
                    leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
                    if (leap and d > 29) or (not leap and d > 28):
                        return False
                return True
    return False
"""

# Step 6: Calculate and Print Cyclomatic Complexity
cc = estimate_cyclomatic_complexity(date_code)
print(f"\nCyclomatic Complexity = {cc}")

# Step 7: Interpretation
if cc <= 10:
    level = "✅ Structured and Well Written Code\n✅ High Testability\n✅ Low Cost and Effort"
elif cc <= 20:
    level = "⚠️ Complex Code\n⚠️ Medium Testability\n⚠️ Medium Cost and Effort"
elif cc <= 40:
    level = "❗ Very Complex Code\n❗ Low Testability\n❗ High Cost and Effort"
else:
    level = "❌ Highly Complex Code\n❌ Not Testable\n❌ Very High Cost and Effort"

print("Code Quality Interpretation:")
print(level)

# Step 8: Optional - Print Independent Paths
print("\nIndependent Paths to Test:")
paths = [
    "1. Valid year, valid month, valid day → Valid",
    "2. Valid year, valid month = April, day = 31 → Invalid",
    "3. Valid year, valid month = April, day = 30 → Valid",
    "4. Valid year, month = Feb, leap year, day = 29 → Valid",
    "5. Valid year, month = Feb, leap year, day = 30 → Invalid",
    "6. Valid year, month = Feb, non-leap year, day = 29 → Invalid",
    "7. Year outside range → Invalid"
]
for path in paths:
    print(path)
import re

# Step 1: Date Validation Function
def is_valid_date(d, m, y):
    if 1900 <= y <= 2100:
        if 1 <= m <= 12:
            if 1 <= d <= 31:
                if (m in [4, 6, 9, 11]) and d > 30:
                    return False
                elif m == 2:
                    leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
                    if (leap and d > 29) or (not leap and d > 28):
                        return False
                return True
    return False

# Step 2: Test Cases to Cover Independent Paths
test_cases = [
    (15, 3, 2020),    # Valid date
    (31, 4, 2021),    # April 31 → Invalid
    (30, 4, 2021),    # April 30 → Valid
    (29, 2, 2020),    # Leap year Feb 29 → Valid
    (30, 2, 2020),    # Leap year Feb 30 → Invalid
    (29, 2, 2021),    # Non-leap year Feb 29 → Invalid
    (15, 10, 1800),   # Invalid year
]

# Step 3: Execute Test Cases
print("Date\t\tValid?")
for d, m, y in test_cases:
    result = is_valid_date(d, m, y)
    print(f"{d:02d}-{m:02d}-{y} \t{'✅ Valid' if result else '❌ Invalid'}")


# Step 4: Cyclomatic Complexity Estimator
def estimate_cyclomatic_complexity(code: str) -> int:
    # Basic decision keywords
    decision_keywords = [r'\bif\b', r'\belif\b', r'\bfor\b', r'\bwhile\b',
                         r'\bcase\b', r'\bcatch\b', r'&&', r'\|\|']

    complexity = 1  # Start at 1
    for keyword in decision_keywords:
        matches = re.findall(keyword, code)
        complexity += len(matches)

    return complexity

# Step 5: Date Code as String
date_code = """
def is_valid_date(d, m, y):
    if 1900 <= y <= 2100:
        if 1 <= m <= 12:
            if 1 <= d <= 31:
                if (m in [4, 6, 9, 11]) and d > 30:
                    return False
                elif m == 2:
                    leap = (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))
                    if (leap and d > 29) or (not leap and d > 28):
                        return False
                return True
    return False
"""

# Step 6: Calculate and Print Cyclomatic Complexity
cc = estimate_cyclomatic_complexity(date_code)
print(f"\nCyclomatic Complexity = {cc}")

# Step 7: Interpretation
if cc <= 10:
    level = "✅ Structured and Well Written Code\n✅ High Testability\n✅ Low Cost and Effort"
elif cc <= 20:
    level = "⚠️ Complex Code\n⚠️ Medium Testability\n⚠️ Medium Cost and Effort"
elif cc <= 40:
    level = "❗ Very Complex Code\n❗ Low Testability\n❗ High Cost and Effort"
else:
    level = "❌ Highly Complex Code\n❌ Not Testable\n❌ Very High Cost and Effort"

print("Code Quality Interpretation:")
print(level)

# Step 8: Optional - Print Independent Paths
print("\nIndependent Paths to Test:")
paths = [
    "1. Valid year, valid month, valid day → Valid",
    "2. Valid year, valid month = April, day = 31 → Invalid",
    "3. Valid year, valid month = April, day = 30 → Valid",
    "4. Valid year, month = Feb, leap year, day = 29 → Valid",
    "5. Valid year, month = Feb, leap year, day = 30 → Invalid",
    "6. Valid year, month = Feb, non-leap year, day = 29 → Invalid",
    "7. Year outside range → Invalid"
]
for path in paths:
    print(path)
