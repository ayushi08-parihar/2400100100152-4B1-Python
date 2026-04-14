txt = "Hello, welcome to my world?"
#x = txt.find("welcome")
#print(x)
print(txt.startswith("Hello"))
print(txt.endswith("my"))
t=("H","e","l","o  ")
print("".join(t))
'''.split() returns a list of words in the string, split by whitespace.
.partition() splits the string into three parts: the part before the separator, the separator itself,
 and the part after the separator. It returns a tuple containing these three parts.'''
print(txt.ljust(50,"#"))