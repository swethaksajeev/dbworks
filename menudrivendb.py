import mysql.connector
# con=mysql.connector.connect(user='root',password='root',host='localhost')
# print(con)
#c=con.cursor()
# # Create a database named shop
#
# c.execute('create database shop')
# print('database file created')

# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`

def create():
#     con=mysql.connector.connect(user='root',password='root',host='localhost',database='shop')
#
# c=con.cursor()
#
#     c.execute('''create table Product(product_id int not null primary key,
#                                       name varchar(20),
#                                       brand int,
#                                       category varchar(20),
#                                       price int,
#                                       stock int)''')
#     print('table created')

    product_id = int(input('enter product id: '))
    name = input('enter name : ')
    brand = input('enter brand : ')
    category = input('enter category : ')
    price = int(input('enter price : '))
    stock = int(input('enter stock : '))

    query = 'insert into Product (product_id,name,brand,category,price,stock)values(%s,%s,%s,%s,%s,%s)'
    data = (product_id,name,brand,category,price,stock)
    # con=mysql.connector.connect(user='root',password='root',host='localhost',database='shop')
    # c=con.cursor()
    c.execute(query, data)
    con.commit()
    print('inserted')

def get():
    query='select * from Product'
    c.execute(query)

    records=c.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print('no records found')

def retrieve():
    pass

def update():
    number=int(input('enter the product id : '))
    stock=int(input('enter new stock : '))
    query='update Product set stock=%s where number=%s'
    data=(stock,number)
    c.execute(query,data)
    record=c.fetchone()
    con.commit()
    print('updated')


def delete():
    number=int(input('enter the product id : '))
    query='delete from Product where product_id=%s'
    data=(number,)
    c.execute(query,data)
    con.commit()
    print('deleted')

while(True):
    print('menu driven')
    print('1.add product details')
    print('2.read all products')
    print('3.search a product')
    print('4.update stock')
    print('5.delete product')
    ch=int(input('enter number : '))
    if ch==1:
        create()
    elif ch==2:
        get()
    elif ch==3:
        retrieve()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    else:
        print('invalid choice')
        exit()


# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit