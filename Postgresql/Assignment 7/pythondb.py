import psycopg2

con = psycopg2.connect(
            host = "localhost",
            database = "Soren",
            user = "postgres",
            password = "0000")

cur = con.cursor()

cur.execute("insert into students(roll,name,college,phone) values(4,'Navneet','RCC',58745512356)")
cur.execute("select roll,name,college,phone from students")

row = cur.fetchall()

for i in row:
    print(f"roll {i[0]} name {i[1]} college {i[2]} phone {i[3]}")

con.commit()
cur.close()

con.close()
