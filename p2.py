# WAP to convert the Upper case into Lower case in a given string by user

# 1. Prompt the user to enter a string
user_input = input("Enter a string: ")

# 2. Convert the input string to lowercase using the .lower() method
# Strings in Python are immutable, so a new string is returned.
lowercase_string = user_input.lower()

# 3. Print the original and the new lowercase string
print(f"Original String: {user_input}")
print(f"Lowercase String: {lowercase_string}")
