import sqlite3
from statistics import mean
from random import randint
conn=sqlite3.connect(r'data.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS test (
    id int,
    date1 int,
    date2 int);''')
#conn.commit()#подтвреждение операции
conn.commit()
# users=[]
# for i in range(1000):
#     users.append((i,randint(-1000,10000),randint(-1000,10000)))
# cur.executemany("INSERT INTO test VALUES(?,?,?);",users)
# conn.commit()

cur.execute("SELECT date1 FROM test;")
out=cur.fetchall()
a = [out[i][0] for i in range(len(out))]
print(a)
print(max(out), min(out),mean(a))

cur.execute("SELECT date2 FROM test;")
out=cur.fetchall()

print(max(out),min(out),mean(a))

