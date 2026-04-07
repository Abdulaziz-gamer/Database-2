import sqlite3 as sq

con = sq.connect("baza.db")
cur = con.cursor()

con.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGET,
    ism TEXT,
    fam TEXT,
    yosh INTEGER,
    course INTEGER
)""")

cur.execute("""INSERT INTO users(id, ism, fam, yosh, course) VALUES (11, "Anvar", "Olimov", 18, 2)""")
cur.execute("""INSERT INTO users(id, ism, fam, yosh, course) VALUES (22, "Akmurod", "Qurbonmurodov", 15, 1)""")
cur.execute("""INSERT INTO users(id, ism, fam, yosh, course) VALUES (22, "Hakim", "Salimov", 21, 4)""")

con.commit()
con.close()