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


#Date created: 18/10/2023
#Last Revision: 18/10/2023
#Purpose: Gives directory information being the directory provided by a user

#some code is commented until i can understand it a bit more and fix it

# Import modules
import os
import subprocess

# Declaration of functions
#Not working properly will review it and fix it later
#def prepare_test_directory(directory_name):
#    try:
#        os.makedirs(directory_name)  # Create the main directory
#        for i in range(1, 4):
#            subdirectory = f"{directory_name}_{i:02d}"
#            os.makedirs(os.path.join(directory_name, subdirectory))  # Create sub-directories
#        print(f"Test directory '{directory_name}' created successfully.")
#    except FileExistsError:
#        print(f"Directory '{directory_name}' already exists. Aborting.")

#test_directory_name = input("Enter the name for the test directory: ")
#prepare_test_directory(test_directory_name)

def list_directory_contents(user_path, output_file):
    with open(output_file, "w") as file:
        for (root, dirs, files) in os.walk(user_path):
             # Write the current directory (root) to the file
            file.write(f"==root==\n{root}\n")
            # Write the sub-directories (dirs) to the file
            file.write("==dirs==\n")
            file.writelines([f"{os.path.join(root, d)}\n" for d in dirs])
            # Write the files in the current directory (files) to the file
            file.write("==files==\n")
            file.writelines([f"{os.path.join(root, f)}\n" for f in files])


# Gives a java error everytime it tries to launch libre writer
#def open_with_libreoffice(file_path):
#    try:
#       subprocess.run(["libreoffice", "--writer", file_path])
#    except FileNotFoundError:
#        print("LibreOffice not found. Please make sure LibreOffice is installed and in your system's PATH.")


#NOTE: The if __name__ == "__main__": block ensures that the code inside it is executed only when the script is run directly 
# and not when it's imported as a module into other scripts. 
# This is a common practice in Python to make your code reusable and modular.

# Main
if __name__ == "__main__":
    # Read user input for the directory path
    user_input_path = input("Enter the directory path (e.g., 'home/YOUR_USERNAME/Desktop': ")
    
    # Read user input for the output file path
    output_file_path = input("Enter the output file name (e.g., 'output.txt': ")

    if os.path.exists(user_input_path):
        # Call the function to list directory contents and write to the output file
        list_directory_contents(user_input_path, output_file_path)
        print(f"Directory contents saved to {output_file_path}")
        #open_with_libreoffice(output_file_path)         
    else:
        print("The provided directory path does not exist.")
