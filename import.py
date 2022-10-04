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

class import_export_BD():
    def __init__(self):
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
    
    def import_to_BD(path_file_excel: str, bd_table_name: str, exists: str = 'replace', index:bool =False):
        file=pd.ExcelFile(path_file_excel)
        print(file.sheet_names)
        df=file.parse()
        df.to_sql(bd_table_name, conn,if_exists=exists,index=index)
        conn1.commit()
        conn1.close()

    def export_from_BD():
        pass

#IEBD = import_export_BD()
#IEBD.import_to_BD('acc_2.xlsx', 'acc_kern_not_stat')