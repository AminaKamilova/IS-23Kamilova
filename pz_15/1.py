import sqlite3 as sq
from data_users import info_users

with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS enterprises (
    Enterprise_code INTEGER PRIMARY KEY AUTOINCREMENT,
    Business_name TEXT NOT NULL,
    Address TEXT,
    Branches INTEGER,
    Total_number_of_staff INTEGER,
    Total_cost_of_equipment INTEGER,
    Volume_of_products INTEGER,
    Registration_date TEXT
    )""")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT OR REPLACE INTO enterprises VALUES(?, ?, ?, ?, ?, ?, ?, ?)", info_users)

with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"SELECT * FROM enterprises WHERE Branches BETWEEN 8 AND 2")

with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"SELECT * FROM enterprises WHERE Volume_of_products > 87")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"SELECT * FROM enterprises WHERE Total_number_of_staff < 3000")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"UPDATE enterprises SET Business_name = 'PPP' WHERE Branches > 5")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"UPDATE enterprises SET Address = 'ул.Домодедово' WHERE Volume_of_products > 85")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"UPDATE enterprises SET Registration_date = '01.01' WHERE Enterprise_code BETWEEN 1900000 AND 1907680")
with sq.connect('Промышленность.db') as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM enterprises WHERE Branches = 5")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"DELETE FROM enterprises WHERE Branches = 7")
with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    cur.execute(f"DELETE FROM enterprises WHERE Volume_of_products = 89")

