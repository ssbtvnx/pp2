import psycopg2
import csv

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    port = 5432,
    database = 'postgres'
)

cur = conn.cursor()

def inputData():
    id = input("input the id: ")
    name = input("input the name: ")
    phone = input("input the phone: ")
    insert = "INSERT INTO phonebook VALUES(%s, %s, %s);"
    cur.execute(insert,(id, name, phone))

def datafromCSV():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            id, name, phone = row
            cur.execute('INSERT INTO phonebook(id, name, phone) VALUES(%s, %s, %s)', (id, name, phone))
            conn.commit()

inputData()
datafromCSV()

conn.commit()

cur.close()
conn.close()