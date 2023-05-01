import psycopg2 as ps

sql = '''
SELECT * FROM phonebook
WHERE 
'''

conn = ps.connect(host = 'localhost',
                  database = 'postgres',
                  string = 'postgres',
                  password = 'delete',
                  port = 5432
)

cur = conn.cursor()


ans = input(r"do you want to search by phone/name:")
if ans == 'phone':
        sql+="phone"
        print("Enter number")
        number=int(input())
        print("""Select option:
        1-phone is equal to number
        2-phone starts with the number
        3-phone ends with the number
        4-phone contains the number""")
        mode1=int(input())
        if mode1==1:
            sql+="='{}'".format(number)
        elif mode1==2:
            sql+=" iLIKE '{}%'".format(number)
        elif mode1==3:
            sql+=" iLIKE '%{}'".format(number)
        else:
            sql+=" iLIKE '%{}%'".format(number)
elif ans == 'name':
        sql += "name"
        print("Enter string")
        string = input()
        print("""Select option:
        1-name is equal to string
        2-name starts with the string
        3-name ends with the string
        4-name contains the string""")
        mode1=int(input())
        if mode1==1:
            sql+="='{}'".format(string)
        elif mode1==2:
            sql+=" iLIKE '{}%'".format(string)
        elif mode1==3:
            sql+=" iLIKE '%{}'".format(string)
        else:
            sql+=" iLIKE '%{}%'".format(string)
cur.execute(sql)
print(cur.fetchall())
    
conn.commit()


cur.close()
conn.close()