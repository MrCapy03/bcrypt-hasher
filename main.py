import bcrypt
import os

def hash_password(password: str, salt_rounds: int = 10):
    # Generate a salt using the same salt rounds as JavaScript (salt_rounds = 10)
    salt = bcrypt.gensalt(rounds=salt_rounds)

    # Hash the password using the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')

# Example usage
username = input("Please input your username:")
password = input("Please input your password:") # This should be the password you want to hash
hashed_password = hash_password(password)

def get_unique_filename(filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}({counter}){extension}"
        counter += 1
    return new_filename

# Create unique filenames for both output files
output_filename = get_unique_filename('output.txt')
private_output_filename = get_unique_filename('PRIVATE_OUTPUT.txt')

# Write to the unique output.txt file
with open(output_filename, 'w') as f:
    f.write("BEWARE OF WHO YOU SHARE THIS WITH, IT MAY COMPROMISE YOUR DATA.\n")
    f.write("Username: " + username + "\n")
    f.write("Hashed Password: " + hashed_password + "\n")

# Write to the unique PRIVATE_OUTPUT.txt file
with open(private_output_filename, 'w') as f:
    f.write("WARNING THIS CONTAINS YOUR PASSWORD AS PLAIN TEXT, DO NOT SHARE IT, THE MERE PURPOSE OF THIS FILE IS TO CONFIRM IF THE HASHED PASSWORD IS THE DESIRED ONE.\n")
    f.write("Username: " + username + "\n")
    f.write("Password: " + password + "\n")
    f.write("Hashed Password: " + hashed_password + "\n")
