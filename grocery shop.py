import pyttsx3
z = pyttsx3.init()
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='satyam',database='grocery')
if conn.is_connected():
    print('successfully connected ')
    z.say('successfully connected to grocery databases and i am  your assitant')
    z.runAndWait()
cursor=conn.cursor()


print('grocery shop management system')
print('1.login')
print('2.exit')
z.say('1.login')
z.say('2.exit')
z.runAndWait()
z.runAndWait()


choice=int(input('enter your choice:'))
z.say('enter your choice')
z.runAndWait()

if choice==1:
    
    while 1>0 :
        print('grocery shop')
        z.say('1 for enter new customer,2 for new product,3 customer details,4 product details,5 worker details,6 for exist')
        z.runAndWait()
        print('1.add new customer ')
        print('2.product new ')
        print('3.cusromer details')
        print('4.product details ')
        print('5.worker details')
        
        print('6.exit')
        
        
        choice=int(input('enter the choice'))
        if choice==1:
      
          a=input('phone number')
          z.say('enter phone number')
          z.runAndWait()
          b=input('customer name')
          z.say('customer name')
          z.runAndWait()
          c=input('cost')
          s="INSERT INTO customer_details(phone_no,cust_name,cost) values(%s,%s,%s)"
          b1=(a,b,c)
          cursor.execute(s,b1)
          conn.commit()
          z.say('your task is completed')
          z.runAndWait()


        

        elif choice==3:
            cursor.execute("select * from customer_details; ")
            row=cursor.fetchone()
            while row is not None:
               print(row)
               row=cursor.fetchone()
            z.say(z,'your task is completed')
            z.runAndWait()

        elif choice==2:
          a=input('product name')
          b=input('cost')
          
          s="INSERT INTO product(productname,productcost) values(%s,%s)"
          b1=(a,b)
          cursor.execute(s,b1)
          conn.commit()
          z.say('your task is completed')
          z.runAndWait()
          
        elif choice==4:
            cursor.execute("select * from product ; ")
            row=cursor.fetchone()
            while row is not None:
               print(row)
               row=cursor.fetchone()
            z.say('your task is completed')
            z.runAndWait()
        
        elif choice==5:
            cursor.execute("select * from worker ;")
            row= cursor.fetchone()
            while row is not None:
                print(row)
                row=cursor.fetchone()
            z.say('your task is completed')
            z.runAndWait()    
                
            
    
            

              
        elif choice==6:
             z.say('your task is completed and you gone exist from programme')
             z.runAndWait()
             exit()
            

            
                            

   
        
            
if choice==2:
    z.say('thanks yous')
    z.runAndWait()
    exit()
