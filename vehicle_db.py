#define a class to perform database operations on vehicle table.
#create a class named VehicleListCreateRetrieveUpdateDelete and define methods

# list() --> for reading all records
# create()-->for creating a new record
# retrieve(id)-->for reading a specific record
# update(id,data)-->for updating a specific record
# delete(id)-->for deleting a specific record


import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user='root',password='root',host='localhost',database='vehicle_db')
        print(self.connection)
        self.cursor=self.connection.cursor()
        print('successfully connected')
    def list(self):
        query='select * from vehicle'
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print('no record found')
    def create(self,brand,model,type,price,year):
        query='insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)'
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print('data inserted successfully')

    def retrieve(self,id):
        query='select * from vehicle where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        records=self.cursor.fetchone()
        if records:
            for row in records:
                print(records)
        else:
            print('no records found')

    def update(self,id,brand,model,type,price,year):
        query='update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s'
        data=(brand,model,type,price,year,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: #if no updation rowcount returns 0
            print('updated successfully')
        else:
            print('no record found')

    def delete(self,id):
        query='delete from vehicle where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: #if no updation rowcount returns 0
            print('data is deleted')
        else:
            print('no record found')

vehicle_instance=VehicleListCreateRetrieveUpdateDelete()
vehicle_instance.list()
# vehicle_instance.create('tata','puch','sedan',600000,2026)
vehicle_instance.retrieve(1)
vehicle_instance.delete(2)
vehicle_instance.update(3,'benz','h11','sedan',800000,2020)