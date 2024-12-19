import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    if length < (include_uppercase + include_digits + include_symbols + 1):
        return "Error: Password length is too short to include all selected character types."
    
    # At least one character from each selected set
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from all allowed characters
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password += [random.choice(characters) for _ in range(length - len(password))]
    
    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# User Input for Password Preferences
print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired password length (e.g., 12): "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_symbols = input("Include special symbols? (yes/no): ").strip().lower() == 'yes'

    # Generate and Display the Password
    password = generate_password(length, include_uppercase, include_digits, include_symbols)
    print(f"\nGenerated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
