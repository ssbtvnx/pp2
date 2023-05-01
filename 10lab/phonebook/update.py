import psycopg2

#update
sql_update_name = '''
    UPDATE phonebook SET name = %s WHERE id = %s;
'''

sql_update_phone = '''
    UPDATE phonebook SET phone = %s WHERE id = %s;
'''


conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    port = 5432,
    database = 'postgres'
)

cur = conn.cursor()


def updateData():
    p = input('which parameter do you want to update?[phone/name]: ')
    id = input('enter id of the parameter which you want to delete:  ')
    if p == 'phone':
        phone = input('enter new phone: ')
        cur.execute(sql_update_phone, (phone, id))
    elif p == 'name':
        name = input('enter new name: ')
        cur.execute(sql_update_name, (name, id))
    else:
        print('error, try again')

updateData()

conn.commit()

cur.close()
conn.close()