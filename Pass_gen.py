import random
import string
import secrets

# Original character sets
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# Function to generate the password
def generate_password(nr_letters, nr_symbols, nr_numbers, length):
    password_list = []

    # Add random letters
    for _ in range(nr_letters):
        password_list.append(secrets.choice(letters))

    # Add random symbols
    for _ in range(nr_symbols):
        password_list.append(secrets.choice(symbols))

    # Add random numbers
    for _ in range(nr_numbers):
        password_list.append(secrets.choice(numbers))

    # Add random characters to meet the total length
    while len(password_list) < length:
        password_list.append(secrets.choice(letters + symbols + numbers))

    # Shuffle the list to ensure randomness
    secrets.SystemRandom().shuffle(password_list)
    
    # Convert list to string
    password = ''.join(password_list)
    
    return password

# Function to evaluate password strength
def evaluate_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in symbols for c in password)

    strength = "Weak"
    if length >= 8 and has_lower and has_upper and has_digit and has_symbol:
        strength = "Strong"
    elif length >= 6 and ((has_lower and has_upper) or (has_digit and has_symbol)):
        strength = "Moderate"
    
    return strength

# Main function to handle user interaction
def main():
    print("Welcome to the Advanced PyPassword Generator!")
    try:
        # Get user inputs
        length = int(input("Enter the total length of your password:\n"))
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        
        # Check if inputs are valid
        if nr_letters + nr_symbols + nr_numbers > length:
            raise ValueError("The sum of letters, symbols, and numbers cannot exceed the total length of the password.")
        
        # Generate password
        password = generate_password(nr_letters, nr_symbols, nr_numbers, length)
        
        # Display generated password
        print(f"Generated Password: {password}")
        
        # Evaluate and display password strength
        strength = evaluate_strength(password)
        print(f"Password Strength: {strength}")
        
        # Ask if the user wants to save the password to a file
        save_to_file = input("Would you like to save the password to a file? (yes/no): ").lower()
        if save_to_file == 'yes':
            with open("generated_password.txt", "a") as file:
                file.write(f"Password: {password} | Strength: {strength}\n")
            print("Password saved to generated_password.txt")
        
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()