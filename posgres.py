import psycopg2
import pandas as pd
conn = psycopg2.connect("dbname=bici2023 user=postgres password=postgres")
cur = conn.cursor()
query = "select * from locations where recorded_at between '2019-09-01' and '2020-01-01' limit 100000"
cur.execute(query)
datos = cur.fetchall()
data = pd.DataFrame(datos)
cur.close()
conn.close()
data.head(10)