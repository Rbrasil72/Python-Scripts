#!/usr/bin/env python3

#     _________
#    / ======= \
#   / __________\
#  | ___________ |
#  | | -       | |
#  | |         | |
#  | |_________| |_____________________________________
#  \=____________/   Rodrigo <Sud0Pirat3> Brasil       )
#  / """"""""""" \                                    /
# / ::::::::::::: \                               =D-'
#(_________________)

# Date created: 17/11/2023
# Last Revision: 20/11/2023
# Purpose: Ask for an input from the user to chose from a selection 4 options, to encrypt and decrypt a message, file or contentes inside a file

# Must have cryptography installed | run on the terminal "pip3 install cryptography"
# Must have prettytable installed | run on the terminal "pip3 install prettytable"

# Imported libraries
from cryptography.fernet import Fernet
from prettytable import PrettyTable
import os

# Function that generates the key
def generate_key():
    return Fernet.generate_key()

# Function that loads a encryption key from a file
def load_key(key_file_path):
    return open(key_file_path, "rb").read()

# Function that saves a encryption key to a file
def save_key(key, key_file_path):
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)

# Function to encrypt the file and delete the original
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    # Write the encrypted data to a new file
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    # Removes the original file
    os.remove(file_path)

# Function to Decrypt a file and delete the encrypted file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Writes the decrypted data to a new file
    with open(file_path.replace(".encrypted", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    # Removes the encrypted file
    os.remove(file_path)

# Function to encrypt a message and print the cypher text 
def encrypt_string(plaintext, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(plaintext.encode())
    print("Ciphertext:", encrypted_data.decode())

# Function to decrypt a message and print it in plaintext
def decrypt_string(ciphertext, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(ciphertext)
    print("Decrypted Text:", decrypted_data.decode())

# Function to encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Function to decrypt a folder and its contents
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def display_menu():
    menu = PrettyTable()
    menu.field_names = ["Option", "Description"]
    menu.add_row(["1", "Encrypt a file"])
    menu.add_row(["2", "Decrypt a file"])
    menu.add_row(["3", "Encrypt a message"])
    menu.add_row(["4", "Decrypt a message"])
    menu.add_row(["5", "Encrypt a folder"])
    menu.add_row(["6", "Decrypt a folder"])

    print(menu)

# Main function to handle user input and execution
def main():
    key_file_path = "encryption_key.key"

    # Check if an encryption key file already exists
    if not os.path.isfile(key_file_path):
        # If not, generate a new one
        key = generate_key()
        save_key(key, key_file_path)
    else:
        # If yes, load the key from the file
        key = load_key(key_file_path)

    display_menu()

    # Get the user input
    mode = int(input("Enter the mode: "))

    if mode in [1, 2, 5, 6]:
        # If the entered mode involves a file or folder, prompt the user to input the path
        path = input("Enter the path to the target: ")

    if mode == 1:
        encrypt_file(path, key)
        print("File encrypted successfully.")

    elif mode == 2:
        decrypt_file(path, key)
        print("File decrypted successfully.")

    elif mode == 3:
        plaintext = input("Enter the cleartext string: ")
        encrypt_string(plaintext, key)

    elif mode == 4:
        ciphertext = input("Enter the ciphertext: ")
        decrypt_string(ciphertext.encode(), key)

    elif mode == 5:
        encrypt_folder(path, key)
        print("Folder encrypted successfully.")

    elif mode == 6:
        decrypt_folder(path, key)
        print("Folder decrypted successfully.")

    else:
        print("Invalid mode. Please enter a valid mode (1-6).")

# Entry point to the script
if __name__ == "__main__":
    main()