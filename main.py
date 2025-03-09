import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # Define the length of the password
    password_length = 12
    # Generate the password
    password = generate_password(password_length)
    # Print the generated password
    print(f"Generated password: {password}")