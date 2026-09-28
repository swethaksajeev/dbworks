#define a class to perform database operations on Book table.
#create a class named BookListCreateRetrieveUpdateDelete and define methods

# list() --> for reading all records
# create()-->for creating a new record
# retrieve(id)-->for reading a specific record
# update(id,data)-->for updating a specific record
# delete(id)-->for deleting a specific record


import mysql.connector


class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='root', host='localhost',
                                                  database='dbfilelibrary_db')
        print(self.connection)
        self.cursor = self.connection.cursor()
        print('successfully connected')

    def list(self):
        #reading all records from db table
        query = 'select * from book'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print('no records found')

    def create(self, title, author, price, pages, language):
        query = 'insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)'
        data = (title, author, price, pages, language)
        self.cursor.execute(query, data)
        self.connection.commit()
        print('data inserted successfully')

    def retrieve(self, id):  #for reading specific record
        num = int(input('enter id :'))
        query = 'select * from book where id=%s'
        data = (id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchone()
        if records:
            for row in records:
                print(records)
        else:
            print('no records found')

    def update(self, id, title, author, price, pages, language):
        query = 'update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s'
        data = (title, author, price, pages, language, id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:  #if no updattion rowcount returns 0
            print('updated successfully')
        else:
            print('no record found')

    def delete(self, id):
        query = 'delete from book where id=%s'
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:  #if no updation rowcount returns 0
            print('data is deleted')
        else:
            print('no record found')


book_instance = BookListCreateRetrieveUpdateDelete()

# book_instance.list()
# book_instance.create('jsm','sam',400,300,'english')
# book_instance.retrieve(1)
# book_instance.delete(4)
book_instance.update(7, 'mike', 300, 250, 300, 'hindi')
