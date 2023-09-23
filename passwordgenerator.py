import secrets
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Define the pool of characters to choose from based on complexity
    if length < 8:
        characters = lowercase_letters + uppercase_letters + digits
    elif length < 12:
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a valid length.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")

if __name__ == "__main__":
    main()
