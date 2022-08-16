"""
Script to insert into postgres
"""

import psycopg2
import pandas as pd
from datetime import datetime


conn = psycopg2.connect(
    host="localhost",
    database="ScaleDB",
    user="postgres",
    password="password")

cur = conn.cursor()


# CREATING TABLE -------------------------------------------------------------------------------------------------------
def create_table():
    cur.execute('''DROP TABLE CRW_154''')
    conn.commit()

    tc = '''CREATE TABLE CRW_154 (t_stamp TIMESTAMP, v_id INTEGER, v_desc VARCHAR, v_val FLOAT)'''
    # INTEGER, CHAR, FLOAT
    cur.execute(tc)
    conn.commit()

    conn.close()




# create_table()


# Inserting to TABLE ---------------------------------------------------------------------------------------------------
def insert_t(v_t, v_id, v_desc, v_val):
    tc = f"INSERT INTO CRW_154 (t_stamp, v_id, v_desc, v_val) " \
                   f"VALUES (%(v1)s, %(v2)s, %(v3)s, %(v4)s);"
    # tc = f"INSERT INTO CRW_154 (v_id, v_desc, v_val) " \
     #              f"VALUES (%(v2)s, %(v3)s, %(v4)s);"
    # f"VALUES ({v_t}, {v_id}, {v_desc}, {v_val})"
    # vals = (v_t, v_id, v_desc, v_val)
    vals = {
            'v1': v_t,
            'v2': v_id,
            'v3': v_desc,
            'v4': v_val
            }
    print(vals)
    cur.execute(tc, vals)
    conn.commit()
# insert_t()


df = pd.read_csv('calc_CRW_154_MERGE.csv')


def insert_data():
    cols = list(df.columns)
    print(cols)
    for index, row in df.iterrows():
        t_stamp = row['Channel_Time']
        t_stamp = '24/06/22 ' + t_stamp
        t_val = datetime.strptime(t_stamp, '%d/%m/%y %I:%M:%S %p')
        print(t_val)

        for i, v in enumerate(cols):
            if v == 'Channel_Time' or v == 't_stamp':
                continue
            insert_t(t_val, i, v, row[v])


insert_data()

# get all from table ---------------------------------------------------------------------------------------------------
# def get_all():
#     tc = f"SELECT * FROM Test_Table "
#     cur.execute(tc)
#     qa = cur.fetchall()
#     print(qa)




# get_all()

conn.close()

# end
