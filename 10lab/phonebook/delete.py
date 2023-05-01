import psycopg2

#delete
sql_delete_name = '''
    DELETE FROM phonebook WHERE name = %s;
'''

sql_delete_phone = '''
    DELETE FROM phonebook WHERE phone = %s;
'''

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    port = 5432,
    database = 'postgres',
)

cur = conn.cursor()

def deleteData():
    p = input('by which parameter you would like to delete?[phone/name]: ')
    if p == 'phone':
        phone = input('enter phone: ')
        cur.execute(sql_delete_phone, (phone,))
    elif p == 'name':
        name = input('enter name: ')
        cur.execute(sql_delete_name, (name,))
    else:
        print('no such parameter')

deleteData()

conn.commit()

cur.close()
conn.close()