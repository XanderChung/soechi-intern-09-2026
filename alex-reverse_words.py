def f(text):
    reversed_text =" ".join(reversed(text.split()))
    return reversed_text

# Test Cases
print(f("  the ship   sails at dawn ")) # Expected: "dawn at sails ship the"
print(f("hello   world"))              # Expected: "world hello"