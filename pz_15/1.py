# Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации о промышленных предприятиях
# республики. БД содержит таблицу Предприятия, имеющую следующую структуру записи: Код предприятия,
# Наименование предприятия, Физический адрес, Филиалы (количество филиалов), Общая числ.персонала,
# Общая стоим.оборудования, Объем выпускаемой продукции, Дата регистрации.

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
# with sq.connect('Промышленность.db') as con:
#     cur = con.cursor()
#     cur.executemany("INSERT OR REPLACE INTO enterprises VALUES(?, ?, ?, ?, ?, ?, ?, ?)", info_users)

# with sq.connect('Промышленность.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM enterprises WHERE Branches > 8 OR Volume_of_products = 86")
#     cur.execute("SELECT * FROM enterprises WHERE Volume_of_products > 87")
#     cur.execute("SELECT * FROM enterprises WHERE Total_number_of_staff < 3000")
#     result = cur.fetchall()
#     print("Выборка:")
#     for row in result:
#         print(row)
#
# with sq.connect('Промышленность.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE enterprises SET Business_name = 'PPP' WHERE Branches = 6")
#     cur.execute("UPDATE enterprises SET Address = 'ул.Домодедово' WHERE Volume_of_products > 85")
#     cur.execute("UPDATE enterprises SET Registration_date = '01.01' WHERE Enterprise_code BETWEEN 1900000 AND 1907680")
#     print("UPDATE:")
#     for rows in result:
#         print(rows)
#
# with sq.connect('Промышленность.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM enterprises WHERE Branches = 5")
#     cur.execute("DELETE FROM enterprises WHERE Branches < 2")
#     cur.execute("DELETE FROM enterprises WHERE Volume_of_products = 90")
#     print("DELETE:")
#     for rows1 in result:
#         print(rows1)