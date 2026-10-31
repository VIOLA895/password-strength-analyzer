import string

print("=" * 45)
print("       PASSWORD STRENGTH ANALYZER")
print("=" * 45)

password = input("\nEnter a password to analyze: ")

# Check the password length
length = len(password)

# Check for different character types
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

print("\nPASSWORD ANALYSIS")
print("-" * 45)

print(f"Password length: {length}")
print(f"Contains uppercase letters: {has_uppercase}")
print(f"Contains lowercase letters: {has_lowercase}")
print(f"Contains numbers: {has_digit}")
print(f"Contains symbols: {has_symbol}")