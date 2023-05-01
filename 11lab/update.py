import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'delete',
    port = 5432,
    database = 'postgres'
)

cur = conn.cursor()


def update_phone():
   # Check if the user already exists
    name = input("input the name: ")
    phone = input("input the phone: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s LIMIT 1", (name,))
    result = cur.fetchone()
    # If user exists, update the phone number
    if result:
        id = result[0]
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    else:
        # If user doesn't exist, insert a new user
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

   
update_phone()

conn.commit()

cur.close()
conn.close()