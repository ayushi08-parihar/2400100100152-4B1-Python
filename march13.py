#printing pattern using just method
txt="WELCOME"
print(txt.ljust(50,"#"))
print(txt.rjust(50,"#"))
for x in range(9):
    print("#"*30)
    if x==4:
      print(txt.center(20,"#"))