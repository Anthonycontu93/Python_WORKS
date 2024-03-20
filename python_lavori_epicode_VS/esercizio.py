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
query = """SELECT *
        FROM dimproduct
        """
df = pd.read_sql(query, db_engine)

# attributo per vedere i dati totali (rows, columns)
dati_totali = df.shape

#  metadati / colonne
metadati = df.columns

# primo e ultimo 
primo = df.head(1)
ultimo = df.tail(1)

# stampiamo 5 elementi a caso 
five_random = df.sample(5)
print(five_random)

# seleziono colonna colpri
colori_avl = list(df["Color"].unique())


# peso media prodotti
avg_peso = df["Weight"].mean()
descrizione_colonna = df["Weight"].describe()

#prodotti peso piu 100kg 
filtro = df["Weight"] > 100 
prodotti_piu_100 = df.loc[filtro]

# prodotti costo medio 
media_costo = df["DealerPrice"].describe()

# se prendo 1/4 dei prodotti quanto sarà la media dei prezzi se prendo i più costosi 
# posso utilizzare il metodo describe() perchè suddivide il dataFrame già in diverse % 
lista_descrittiva_prodotto = list(df["DealerPrice"].describe())
# indicizzo la lista oppure le key per la series
costo_min_75x100 = lista_descrittiva_prodotto[6]
print(lista_descrittiva_prodotto, float(costo_min_75x100) )

# filtro la il df per colore colonna 
filtro_colore_blu = df["Color"] == "Blue"
# utilizzo la maschera per creare un altro df solo con colore blue
df_blue = df.loc[filtro_colore_blu]
print(df_blue.head())

# prendo la colonna prezzo e faccio media 
media_prezzo_blue = df_blue["DealerPrice"].mean()
print(media_prezzo_blue)


# prezzo medio prodotti colore rosso e nero 
filtro_rosso_nero = (df["Color"] == "Red") | (df["Color"] == "Black")
filtro_rosso = df["Color"] == "Red"
filtro_nero = df["Color"] == "Black"

prodotti_r_n = df.loc[filtro_rosso | filtro_nero]
r_n = df.loc[filtro_rosso_nero]
print(prodotti_r_n["Color"].unique())


# prezzo medio rosso e nero 
prezzo_medio_r_n = prodotti_r_n["DealerPrice"].mean()

# prezzo massimo per proddotti taglia 42 e peso 10 kg 
filtro_taglia = df["Size"] == "42"
filtro_peso = df["Weight"] > 10 
prod_tagliaepeso_4210 =df.loc[filtro_taglia & filtro_peso]
print(prod_tagliaepeso_4210.sample(2))
max_prezzo = prod_tagliaepeso_4210["DealerPrice"].max()