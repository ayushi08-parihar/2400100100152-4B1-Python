
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def countVowels(str):
    count = 0
    for i in range(len(str)):

        # Check for vowel
        if isVowel(str[i]):
            count += 1
            print(str[i])
    return count

# Driver Code

# string object 
str = 'abc de'

# Total number of Vowels
print(countVowels(str))


