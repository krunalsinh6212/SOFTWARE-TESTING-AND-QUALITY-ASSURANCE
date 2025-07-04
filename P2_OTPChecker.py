def validate_otp(otp):
    length = len(otp)
    if length < 6:
        return "Invalid OTP: Too short"
    elif length > 6:
        return "Invalid OTP: Too long"
    elif not otp.isdigit():
        return "Invalid OTP: Must contain only digits"
    else:
        return "Valid OTP"

# Test Cases from Equivalence Partitioning table
test_cases = [
    "67545678",  # Invalid: > 6 digits
    "9754",      # Invalid: < 6 digits
    "654757",    # Valid: exactly 6 digits
    "213309",    # Valid: exactly 6 digits
    "12a456",    # Invalid: contains non-digit
]

# Execute test cases
print("OTP\t\tResult")
for otp in test_cases:
    result = validate_otp(otp)
    print(f"{otp}\t{result}")
