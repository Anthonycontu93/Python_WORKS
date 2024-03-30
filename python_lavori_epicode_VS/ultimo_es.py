from sqlalchemy import create_engine
import dotenv
import os
import pandas as pd
dotenv.load_dotenv(override=True)
username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('host')
dbname = os.getenv('dbname')

import pandas as pd
dbname = "AdventureWorksDW"
conn_string = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"
db_engine = create_engine(conn_string)
dimemployee = """SELECT *
        FROM dimemployee
        """
df = pd.read_sql(dimemployee, db_engine)
df.shape

dimemployeesalesterritory = """SELECT *
        FROM dimemployeesalesterritory
        """


df2 = pd.read_sql(dimemployeesalesterritory, db_engine)
df2.shape
print(df2.columns)


df_merge = pd.merge(df, df2, on= "EmployeeKey")
print(df_merge.sample(5))

# nuova query 
dimsalesterritory = """SELECT *
        FROM dimsalesterritory
        """

df3 = pd.read_sql(dimsalesterritory, db_engine)

df_merge_merge = pd.merge(df_merge, df3, on = "SalesTerritoryKey")
print(df_merge_merge.sample(5))

print(df_merge_merge.columns)

#country_employee = df_merge_merge.groupby("country")