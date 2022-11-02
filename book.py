import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='librarydb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add bookdetails')
    print('2 view book')
    print('3 search book')
    print('4 update book')
    print('5 delete book')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print('add book')
        bookname=input('enter bookname:')
        author=input("enter author:")
        category=input('enter category:')
        bookchargeperday=input("enter charge:")
        sql='INSERT INTO `book`( `bookname`, `author`, `category`, `bookchargeperday`) VALUES(%s,%s,%s,%s)'
        data=(bookname,author,category,bookchargeperday,)
        mycursor.execute(sql,data)
        mydb.commit()
    if(choice==2):
        print("view book")
        
    elif(choice==3):
        print('search a book')
    elif(choice==4):
        print('update the book')
        
    elif(choice==5):
        print('delete the book')
    elif(choice==6):
        print("exit")
        break