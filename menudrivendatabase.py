# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`

# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit



import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(user='root',password='root',host='localhost')

c = con.cursor()

# Create database
# c.execute('create database shop')
# print('Database created')

# Connect to shop database
con = mysql.connector.connect(user='root',password='root',host='localhost',database='shop')

c = con.cursor()


# c.execute('''Create Table Product(
#     product_id INT NOT NULL PRIMARY KEY,
#     name Varchar(20),
#     brand Varchar(20),
#     category varchar(20),
#     price int,
#     stock int
# )''')
#
# print('Table created')



def create():
    product_id = int(input('Enter product id: '))
    name = input('Enter name: ')
    brand = input('Enter brand: ')
    category = input('Enter category: ')
    price = int(input('Enter price: '))
    stock = int(input('Enter stock: '))

    query = '''insert into Product
               (product_id, name, brand, category, price, stock)
               values (%s, %s, %s, %s, %s, %s)'''

    data = (product_id, name, brand, category, price, stock)

    c.execute(query, data)
    con.commit()

    print('Product inserted successfully')



def get():
    query = 'SELECT * FROM Product'

    c.execute(query)

    records = c.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print('No records found')



def retrieve():
    product_id = int(input('Enter the product id: '))

    query = 'select * from Product where product_id=%s'
    data = (product_id,)

    c.execute(query, data)

    record = c.fetchone()

    if record:
        print(record)
    else:
        print('Product not found')



def update():
    product_id = int(input('Enter the product id: '))
    stock = int(input('Enter new stock: '))

    query = 'update Product set stock=%s where product_id=%s'
    data = (stock, product_id)

    c.execute(query, data)
    con.commit()




def delete():
    product_id = int(input('Enter the product id: '))

    query = 'delete from Product where product_id=%s'
    data = (product_id,)

    c.execute(query, data)
    con.commit()

    if c.rowcount > 0:
        print('Product deleted successfully')
    else:
        print('Product not found')


# Menu-driven program
while True:

    print('\nMENU DRIVEN')
    print('1. Insert Product details')
    print('2. Read all Product details')
    print('3. Search a Product by product_id')
    print('4. Update the stock of a Product')
    print('5. Delete a Product record')
    print('6. Exit')

    ch = int(input('Enter number: '))

    if ch == 1:
        create()

    elif ch == 2:
        get()

    elif ch == 3:
        retrieve()

    elif ch == 4:
        update()

    elif ch == 5:
        delete()

    elif ch == 6:
        exit()
        break

    else:
        print('Invalid choice')