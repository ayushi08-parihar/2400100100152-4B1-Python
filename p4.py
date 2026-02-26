
'''
    result = ""
    i = 0
    while i < len(s):
        # Current character
        char = s[i]
        i += 1
        
        # Next part might be digits
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        # Multiply character by number and add to result
        if num_str:
            result += char * int(num_str)
            
    return result

# Example Usage
print(f"Input: {str}")
print(f"Output: {result}") # Output: aaaabbbbccccc
'''











str = input("Enter a string")
expand_str = ""
for i in range(0, len(str), 2):
  char = str[i]
  freq = int(str[i+1])
  expand_str += char * freq
print("original string ",str)
print(expand_str)


'''str = 'a3b4c5'
expand_str = ""
for i in range(0, len(str), 2):
  char = str[i]
  freq = int(str[i+1])
  expand_str += char * freq
print(expand_str)
'''

