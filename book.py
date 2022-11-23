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
    print('6 :Update the total amount for each book depending on the return date')
    print('7 :.Display the total number of books in each category of book table')
    print('8 : Display the book details where book name starting character contain ')
    print('9 : Exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print('add book')
        bookname=input('enter bookname:')
        author=input("enter author:")
        category=input('enter category:')
        bookchargeperday=input("enter charge:")
        eastablishdate=input("enter date(yyyy-mm-d)")
        sql='INSERT INTO `book`( `bookname`, `author`, `category`, `bookchargeperday`,`eastablishdate`) VALUES(%s,%s,%s,%s,%s)'
        data=(bookname,author,category,bookchargeperday,eastablishdate)
        mycursor.execute(sql,data)
        mydb.commit()
    if(choice==2):
        print("view book")
        sql='SELECT * FROM `book`' 
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i) 
        
    elif(choice==3):
        print('search a book')
        bookname=input("enter bookname:")
        sql="SELECT `id`, `bookname`, `author`, `category`, `bookchargeperday`, `eastablishdate` FROM `book` WHERE `bookname` ='"+bookname+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the book')
        bookchargeperday=input("enter bookchargeperday :")
        bookname=input('enter bookname:')
        author=input("enter author to be updated:")
        category=input('enter categry to be updated:')
        sql="UPDATE `book` SET `bookname`='"+bookname+"',`author`='"+author+"',`category`='"+category+"' WHERE `bookchargeperday`="+bookchargeperday
        mycursor.execute(sql)
        mydb.commit()
        print("data successfully updated")
        
    elif(choice==5):
        print('delete the book')
        bookchargeperday=input("enter charhe:")
        sql='DELETE FROM `book` WHERE `bookchargeperday`='+bookchargeperday
        mycursor.execute(sql)
        mydb.commit()
    elif(choice == 6 ):
        sql = 'SELECT i.`userid`, i.`bookid`, i.`issue date`, i.`return date`,DATEDIFF(i.`return date`,i.`issue date`) AS datediff ,DATEDIFF(i.`return date`,i.`issue date`)*b.bookchargeperday AS TotalAmount FROM `issuebook` i JOIN book b ON i.bookid=b.id'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
         print(i)
    elif(choice==7):
        print('displays Total number of books for each category')

        sql='SELECT COUNT(*) AS totalbookpercategory,`category` FROM `book` GROUP BY `category`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
         print(i)
    elif(choice == 8):
        
        print('Displays the character which you needed ')

        character= input('Enter the starting character of book you need to display : ')

        sql = "SELECT `id`, `bookname`, `author`, `category`, `bookchargeperday` FROM `book` WHERE `bookname` LIKE '"+character+"%'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        for i in result:

            print(i)
        
    elif(choice == 9):
        break