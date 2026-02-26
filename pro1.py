# Program to print the ASCII values of a given string
input_string = "Hello"
for char in input_string:
    # Use the built-in ord() function to get the ASCII value (Unicode code point)
    ascii_value = ord(char)
    print(f"Character: '{char}', ASCII : {ascii_value}")



