#MY PYTHON LIBRARY
#****************************************************************************************************
def intro():
    print ('''☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
                                                A
                                         PROJECT REPORT
                                               ON
                                        BOOK INFORMATION
            *****************************************************************************************
            •+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•+•
                                             CONCEPT USED:
                                            PYTHON PROGRAMMING
                                USAGES OF PYTHON COLLECTION OF DATA TYPE:
                                             •LIST
                                             •TUPLE
                                             •DICTIONARY
            ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
            ==========================================================================================
                                    ===============================
                                      DEVELOPED BY :AYUSHI PARIHAR
                                           
                                    ===============================
            ==========================================================================================
            --------------------------------------------------------------------------------------''')
intro()
opt=input("PRESS ANY KEY TO CONTINUE..........................")
#====================================================================================================
def addrecord():
     name=input("Enter buyer name").upper()
     bname=input("Enter book name").upper()
     code=input("Enter book code")
     price=input("Enter price of book")
     nameau=input("Enter author's name").upper()
     emailid=input("Enter publisher email id").upper()
     bookinfo[name]=(bname,code,price,nameau,emailid)
     print(name,' record inserted successfully ')
#=====================================================================================================
def searchrecord():
      name=input('Enter buyer\'s name to search book information ').upper()
      if name in bookinfo:
          v=list(bookinfo[name].values())
          print("buyer name:",name)
          print("book name : ",v[0])
          print("code of book : ",v[1])
          print("price of book : ",v[2])
          print("author of book : ",v[3])
          print("Publisher email id : ",v[4])
          print('Record displayed successfully ')
      else:
          print('Name not found! ')
#=====================================================================================================
def deleterecord():
      name=input('Enter buyer\'s name to search book information ').upper()
      if name in bookinfo:
          v=list(bookinfo[name].values())
          print("buyer name:",name)
          print("book name : ",v[0])
          print("code of book : ",v[1])
          print("price of book : ",v[2])
          print("author of book : ",v[3])
          print("Publisher email id : ",v[4])
          print('Record displayed successfully ')
          delch=input("Are you sure to delete it (Y/N) ").upper()
          if delch=="Y":
                del bookinfo[name]
                print("Record deleted successfully\a")
      else:
          print('Name not found! ')
#=====================================================================================================
def updaterecord():
       name = input('Enter buyer name to update book  ').upper()
       if name in bookinfo:
            bname = int(input('Input new issued book '))
            bookinfo[name] = bname
            print('Data updated successfully ')
            print(bookinfo)
       else:
            print('Name not found!')

#=====================================================================================================
def displayrecord():
       print("Data displayed:",bookinfo)
#=====================================================================================================
def buyers():
    print("In this Library there are:",len(bookinfo.keys()))
#=====================================================================================================
def searchbook():
    name=input("Enter buyer's name:").upper()
    key=bookinfo.keys()
    if name in key:
        print("The buyer purchased book ",bookinfo[name][0])
    else:
        print("Buyer's record not found")
#=====================================================================================================
def searchauthor():
    name=input("Enter buyer's name:").upper()
    key=bookinfo.keys()
    if name in key:
        print(" Author of book:",bookinfo[name][3])
    else:	
        print("Buyer's record not found")
#=====================================================================================================
def code():
    name=input("Enter buyer's name:").upper()
    key=bookinfo.keys()
    if name in key:
        print("Code of Book:",bookinfo[name][1])
    else:
        print("Buyer's record not found")
#======================================================================================================

def information():
    print('''Library name: ALL TOPPER'S LIBRARY
             Contact No.:-1900180070
             Address:-Chakeri,Kanpur''')

#======================================================================================================

intro()
bookinfo=dict()  # blank dictionary
while True:
        print('''MAIN MENU
               1.Add record
               2.Search record
               3.delete record
               4.update record
               5.show record
               6.Check no. of book buyer
               7.check the book name
               8.check the author's name
               9.check code of book
               10.Information about the Library
               11.Exit''')

        mchoice = int(input('Enter your choice 1-2-3-4-5-6-7-8-9-10 :'))
        if mchoice == 1:
                     addrecord()
        elif mchoice == 2:
                   searchrecord()
        elif mchoice == 3:
                   deleterecord()
        elif mchoice == 4:
                    updaterecord()
        elif mchoice == 5:
                    displayrecord()
        elif mchoice == 6:
                     buyers()
        elif mchoice == 7:
                     searchbook()
        elif mchoice == 8:
                    searchauthor()
        elif mchoice == 9:
                    code()
        elif mchoice == 10:
                    information()
        elif mchoice == 11:
                    print("Thank you for using the program. Have a nice day!")
                    break
        else:
               print('Invalid choice ')
        opt=input("Press any Key to Continue.......................................")                  





            
                                          
