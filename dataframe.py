import sqlite3
from pandas import DataFrame

conn=sqlite3.connect("profile.db")
c=conn.cursor()
c.execute ("""CREATE TABLE if not exists employees(
              id INTEGER,
              first  TEXT,
              last TEXT,
              pay INTEGER
              )""")


    # STEP 2
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")


c.execute("select * from employees")
df=DataFrame(c.fetchall())
df.columns=["ID","first","last","pay"]
c.execute("select * from employees")
print(c.fetchall())  # putting the result into Dataframe

conn.commit()
conn.close()
