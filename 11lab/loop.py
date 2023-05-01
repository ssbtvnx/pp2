import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    database = 'postgres',
    port = 5432
)

cur = conn.cursor()

loop=[]
while True:
    ans = input('do you want to insert data? ')
    if ans == 'no':
        break
    user = input().split()
    if len(user)>2:
        loop.append(user)
        continue
    if not user[1].isdigit():
        loop.append(user)
        continue
        
    cur.execute("INSERT INTO phonebook VALUES (DEFAULT, %s, %s)",(user))
    
conn.commit()


cur.close()
conn.close()