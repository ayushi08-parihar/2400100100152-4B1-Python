str = input("Enter a string")
result = ""
for i in range(0, len(str),2):
  ch=str[i]
  num=int(str[i+1])
  result+=ch*num
print("original string ",str)
print("expanded string ",result)
