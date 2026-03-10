'''Write a python program to ask for a probable password string from the 
user and check if it is suitable for a strong password. It must contain: 
i) At least 8 characters 
ii) Must contain capital and lower-case character 
iii) Must contain symbol and digit '''
password = input("Enter a password: ")
if len(password) < 8:   
    print("Password must be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")   
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
    print("Password must contain at least one symbol.")
else:
    print("Password is strong.")
    