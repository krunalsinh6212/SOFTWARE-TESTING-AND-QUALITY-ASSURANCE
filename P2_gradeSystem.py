# Main program

def getGrade(mark):
    if 90 <= mark <= 100:
        return ("Outstanding", "O", 10.00)
    elif 80 <= mark <= 89:
        return ("Excellent", "A+", 9.00)
    elif 70 <= mark <= 79:
        return ("Very Good", "A", 8.00)
    elif 60 <= mark <= 69:
        return ("Good", "B+", 7.00)
    elif 50 <= mark <= 59:
        return ("Above Average", "B", 6.00)
    elif 40 <= mark <= 49:
        return ("Pass", "P", 5.00)
    else:
        return ("Fail", "F", 0.00)

# Define test cases (mark, expected_description, expected_grade, expected_point)

test_cases = [
    (95, "Outstanding", "O", 10.00),
    (85, "Excellent", "A+", 9.00),
    (75, "Very Good", "A", 8.00),
    (65, "Good", "B+", 7.00),
    (55, "Above Average", "B", 6.00),
    (45, "Pass", "P", 5.00),
    (30, "Fail", "F", 0.00),
    (100, "Outstanding", "O", 10.00),
    (0, "Fail", "F", 0.00),
    (89, "Excellent", "A+", 9.00)
]

# Run test cases

for i, (mark, exp_desc, exp_grade, exp_point) in enumerate(test_cases):
    desc, grade, point = getGrade(mark)
    assert (desc, grade, point) == (exp_desc, exp_grade, exp_point), \
        f"Test case {i + 1} failed: mark = {mark}, expected = ({exp_desc}, {exp_grade}, {exp_point}), got = ({desc}, {grade}, {point})"

print("All grade test cases passed.")
