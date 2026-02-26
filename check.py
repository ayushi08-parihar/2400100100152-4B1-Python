a=int(input("Enter a number"))
#check if number is in betwween 1 and 100
'''if a>1 and a<100:
    print(a,"is in range")
else:
    print(a,"is out of range")'''
#check if number is in betwween 1 and 100 using for loop
for i in range(1,100):
    if a==i:
        print(a,"is in range")
        break   
else:    print(a,"is out of range")   

