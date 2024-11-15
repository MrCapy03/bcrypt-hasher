# Password Hasher Utility

# Introduction

Welcome to the **Password Hasher Utility**! This is a small, simple tool for hashing passwords using **bcrypt** — a secure and well-established password hashing algorithm and it helps you securely hash your passwords to store in your application or database.

### Developed by: 
This utility was developed by **@mrcapy03**. Feel free to reach out with any questions or suggestions for improvement.


### What does it do?

1. **Hash your password**: The utility takes your password and generates a secure, hashed version of it using bcrypt.
2. **Create output files**: It automatically saves the hashed password along with the username in a text file, making it easier to manage your hashes.
3. **Protect your data**: It creates two files inside a folder called `output`:
   - `output.txt`: Contains the hashed password with a warning not to share it with others.
   - `PRIVATE_OUTPUT.txt`: Includes the raw password (for verification purposes) along with the hashed version, so you can confirm the hash matches the desired result.

# How to Use

### Prerequisites:
- **bcrypt** library needs to be installed. If it's not already installed, the script will automatically check for it and install it for you (Only in Windows).

## Windows

### Steps:

1. **Run the script**: Simply run the `win-run.bat`. file.
2. **Input your username and password**: The program will ask you to input your username and password. It’s that easy!
3. **Check your output files**:
   - Once the script runs, you'll find two output files in the same directory:
     - **`output.txt`** – Contains the hashed password and a warning message.
     - **`PRIVATE_OUTPUT.txt`** – Contains the raw password (not for sharing) and the hashed password for verification.

## Linux

### Steps:

1. **Check requirements**: Confirm you have **bcrypt** installed, if not run: `pip install -r requirements.txt`.
2. **Run the script**:
    - Open a terminal
    - Navigate to the file path
    - Run the script using: `python main.py`
3. **Input your username and password**: The program will ask you to input your username and password.
4. **Check your output files**:
   - Once the script runs, you'll find two output files in the same directory:
     - **`output.txt`** – Contains the hashed password and a warning message.
     - **`PRIVATE_OUTPUT.txt`** – Contains the raw password (not for sharing) and the hashed password for verification.

# Outputs

## Example output in `output.txt`:

BEWARE OF WHO YOU SHARE THIS WITH, IT MAY COMPROMISE YOUR DATA.

Username: john_doe

Hashed Password: $2b$10$T9rjG/x5Zv3XNdwTjH0Foe9p/0mbHzVpFlQmc9qKgP5O1n8tPwiTa


## Example output in `PRIVATE_OUTPUT.txt`:

WARNING THIS CONTAINS YOUR PASSWORD AS PLAIN TEXT, DO NOT SHARE IT, THE MERE PURPOSE OF THIS FILE IS TO CONFIRM IF THE HASHED PASSWORD IS THE DESIRED ONE.

Username: john_doe

Password: mysecretpassword

Hashed Password: $2b$10$T9rjG/x5Zv3XNdwTjH0Foe9p/0mbHzVpFlQmc9qKgP5O1n8tPwiTa

# Notes

- The password is hashed using **bcrypt** with 10 salt rounds (default), which is a good balance between speed and security.
- Always keep **`PRIVATE_OUTPUT.txt`** safe. It contains your plain text password and should not be shared.
- The hashed password in `output.txt` is safe to store and share with the backend.

# License:

## GNU AGPLv3
More info can be found in LICENSE file.
