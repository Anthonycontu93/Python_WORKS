import json as j
 

file_path = "C:/Users/HOME/Desktop/python_lavori_epicode_VS/Mappa-dei-pub-circoli-locali-in-Italia.json"

f = j.load(open(file_path, "r", encoding="latin1"))
print(j.dumps(f, indent = 4))

for i in f:
    print(i)


# Esaminiamo il dataset: • quanti dati ci sono in totale? • quali sono i metadati? • stampiamo il primo elemento 
# • stampiamo l'ultimo elemento • riusciamo a stampare un elemento a caso? • quali sono gli anni di inserimento presenti?
# • quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46? 
# • quante attività ci sono nella provincia di Vicenza? • quante enoteche ci sono, e come si chiamano?
