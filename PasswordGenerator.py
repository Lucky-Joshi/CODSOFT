import random
import string

#Function to generate a random password of user's dsire length
def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print(f"Generated Password: {password}")

main()