"""
Script to connect with postgres database
"""

import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="ScaleDB",
    user="postgres",
    password="password")

cur = conn.cursor()


def create_table():
    tc = '''CREATE TABLE Test_Table_Tim (
                        t_stamp
                        v_id INTEGER,
                        val Float
                        )'''
    cur.execute(tc)
    conn.commit()

    conn.close()


def insert_t():
    tc = f"INSERT INTO Test_Table (v_id, val) " \
                   f"VALUES (10, 10125)"
    cur.execute(tc)
    conn.commit()


def get_all():
    tc = f"SELECT * FROM Test_Table "
    cur.execute(tc)
    qa = cur.fetchall()
    print(qa)


create_table()
# insert_t()
# get_all()

conn.close()

# end
