# file_handling_assignment.py

# Step 1: File Creation - Writing to a file
try:
    # Create a new text file and open it in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text, including strings and numbers
        file.write("I am putting all my focus on python.\n")
        file.write("I will have 6 hours a day for python study\n")
        file.write("Python is fun!\n")
    print("File created and written successfully.")

except PermissionError:
    print("Permission denied: unable to write to the file.")

finally:
    print("File writing operation completed.\n")


# Step 2: File Reading and Display
try:
    # Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        print(file.read())

except FileNotFoundError:
    print("File not found: unable to read from the file.")
except PermissionError:
    print("Permission denied: unable to read the file.")
finally:
    print("File reading operation completed.\n")


# Step 3: File Appending - Adding more content to the file
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("Appending is adding text to a line.\n")
        file.write("7 of my dogs are male\n")
        file.write("Appending more content is easy!\n")
    print("Additional content appended successfully.")

except PermissionError:
    print("Permission denied: unable to append to the file.")
finally:
    print("File appending operation completed.\n")


# Step 4: Read and display the file again after appending
try:
    # Open the file in read mode ('r') to display the updated content
    with open("my_file.txt", "r") as file:
        print("Updated contents of 'my_file.txt' after appending:")
        print(file.read())

except FileNotFoundError:
    print("File not found: unable to read from the file.")
except PermissionError:
    print("Permission denied: unable to read the file.")
finally:
    print("Final file reading operation completed.\n")
