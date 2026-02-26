def expand_string(s):
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
input_str = "a3b4c5"
output = expand_string(input_str)
print(f"Input: {input_str}")
print(f"Output: {output}") # Output: aaaabbbbccccc
