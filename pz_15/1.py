import sqlite3 as sq

with sq.connect('Промышленность.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    Enterprise_code INTEGER PRIMARY KEY AUTOINCREMENT,
    Business_name TEXT NOT NULL,
    Address TEXT,
    Branches INTEGER,
    Total_number_of_staff INTEGER,
    Total_cost_of_equipment INTEGER,
    Volume_of_products INTEGER,
    Registration_date TEXT
    )""")