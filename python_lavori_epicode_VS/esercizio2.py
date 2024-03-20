from sqlalchemy import create_engine
import dotenv
import os
import pandas as pd
import matplot
dotenv.load_dotenv(override=True)
username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('host')
dbname = os.getenv('dbname')

import pandas as pd
dbname = "AdventureWorksDW"
conn_string = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"
db_engine = create_engine(conn_string)
query = """SELECT *
        FROM dimproduct
        """
df = pd.read_sql(query, db_engine)


# nome inglese e costo produzione (StandardCost) dei prodotti taglia 42 oltre 10kg e colore argento 
#print(df.head(3))

#maschere
filtro_taglia = df["Size"] == "42"
filtro_peso = df["Weight"] > 10 
filtro_colore_arg = df["Color"] == "Silver"

# and logico per escludere tutti gli altri 
prod_size_weight_silver =df.loc[filtro_taglia & filtro_peso & filtro_colore_arg]

# indexing 
#print(prod_size_weight_silver[["StandardCost","EnglishProductName"]])
#print("\n"*2)
new_df = prod_size_weight_silver[["StandardCost","EnglishProductName"]]

print(new_df, "\n"*1)

#print(prod_size_weight_silver.columns)

#ultimi 20 elementi del dataset 
ultimi_20 = df.tail(20)
# si può fare senza iloc??? 
print(ultimi_20.iloc[:, 1:18:2])

ultimi_standard_price = ultimi_20[["StandardCost","DealerPrice"]]
# il patter è che si ripete per 4 taglie ma non sempre 
print("\n"*1,ultimi_standard_price.tail(4).plot() )
#ultimi_price = ultimi_20["DealerPrice"]

#print(ultimi_price.unique(), "\n"*1, ultimi_standard.unique())