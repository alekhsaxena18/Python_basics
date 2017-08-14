import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Omshiva@321' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("create table if not exists store (items TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Omshiva@321' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("insert into store values(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("water",10,5)

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Omshiva@321' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("select * from store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Omshiva@321' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("delete from store where items =%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Omshiva@321' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("update store set quantity=%s,price=%s where items=%s",(quantity,price,item))
    conn.commit()
    conn.close()




create_table()
insert('apple',10,20)
#delete('apple')
update(20,65,'apple')

print(view())
