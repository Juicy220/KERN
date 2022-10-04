import pandas as pd
import psycopg2
from sqlalchemy import create_engine
file=pd.ExcelFile('acc_2.xlsx')
print(file.sheet_names)
df=file.parse()

conn_string='postgresql://postgres:87900@localhost/kern'
db=create_engine(conn_string)
conn=db.connect()
conn1=psycopg2.connect(
    database="kern",
    user="mkovalev",
    password="12345",
    host="127.0.0.1",
    port="5432"
)

conn1.autocommit=True

df.to_sql('acc_kern_not_stat',conn,if_exists='replace',index=False)
conn1.commit()
conn1.close()