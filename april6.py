#Python program to read a file line by line and store it in a list
file_path = 'example.txt'  # Replace with your file path
lines = []
with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  # Remove any leading/trailing whitespace
print(lines)  # Print the list of lines
