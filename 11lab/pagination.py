import psycopg2 as ps

sql = '''
SELECT * FROM phonebook
'''

conn = ps.connect(host = 'localhost',
                  database = 'postgres',
                  user = 'postgres',
                  password = 'delete',
                  port = 5432 
)

cur = conn.cursor()

ans = input("Need offset? ")
if ans == "yes":
    print("Enter offset: ")
    offset = int(input())
    sql += " OFFSET {}".format(offset)
ans = input("Need limit? ")
if ans == "yes":
    print("Enter limit: ")
    limit = int(input())
    sql += " LIMIT {}".format(limit)
sql += ";"
cur.execute(sql)
print(cur.fetchall())

    
conn.commit()


cur.close()
conn.close()