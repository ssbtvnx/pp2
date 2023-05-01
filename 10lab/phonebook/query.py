import psycopg2

#update
sql_update_name_id = '''
    UPDATE phonebook SET name = %s, id = %s WHERE phone = %s;
'''

sql_update_phone_id = '''
    UPDATE phonebook SET phone = %s, id = %s WHERE name = %s;
'''

sql_update_name_phone = '''
    UPDATE phonebook SET name = %s, phone = %s WHERE id = %s;
'''
#select
sql_select_all_records = '''
    SELECT * FROM phonebook;
'''

sql_select_record_by_id = '''
    SELECT * FROM phonebook WHERE id = %s;
'''

sql_select_record_by_name = '''
    SELECT * FROM phonebook WHERE name = %s;
'''

sql_select_record_by_phone = ''' 
    SELECT * FROM phonebook WHERE phone = %s;
'''


conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    port = 5432,
    database = 'postgres'
)

cur = conn.cursor()

def table():
    cur.execute(
        '''
        CREATE TABLE phonebook(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
        );
        '''
    )

def updateData():
    p = input('what parameter do you have: ')
    if p == 'phone':
        phone = input('enter given phone number: ')
        name = input('enter new name: ')
        id = input('enter new ID: ')
        cur.execute(sql_update_name_id, (name, id, phone))
    elif p == 'name':
        name = input('enter given name: ')
        phone = input('enter new phone: ')
        id = input('enter new ID: ')
        cur.execute(sql_update_phone_id, (phone, id, name))
    elif p == 'id':
        id = input('enter given id: ')
        phone = input('enter new phone: ')
        name = input('enter new name: ')
        cur.execute(sql_update_name_phone, (name, phone, id))
    else:
        print('error, try again')


def queryData():
    p = input("what parameter do you want to execute?[all/id/name/phone]: ")
    if p == 'all':
        cur.execute(sql_select_all_records)
        print(cur.fetchall())
    elif p == 'id':
        id = input("input id of the record: ")
        cur.execute(sql_select_record_by_id, (id,))
        print(cur.fetchall())
    elif p == 'name':
        name = input("input the name of the record: ")
        cur.execute(sql_select_record_by_name, (name,))
        print(cur.fetchall())
    elif p == 'phone':
        phone = input("input the phone of the record: ")
        cur.execute(sql_select_record_by_phone, (phone,))
        print(cur.fetchall())
    else:
        print("no such parameter")




#updateData()
queryData()
conn.commit()

cur.close()
conn.close()