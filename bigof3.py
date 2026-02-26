a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=int(input("Enter a third number"))
if a>b and a>c:
  print(a,"is bigger than")   
elif b>a and b>c:
  print(b,"is bigger than")   
elif c>a and c>b:
  print(c,"is bigger than") 
else:  print("invalid input") 
