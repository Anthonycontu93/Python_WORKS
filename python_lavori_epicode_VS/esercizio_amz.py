import pandas as pd 


path = "C:/Users/HOME/Desktop/python_lavori_epicode_VS/beginner_datasets/amazon.csv"

amazon = pd.read_csv(path)

#Valutiamo la dimensione del dataset • Visualizziamo dieci righe a caso; • Osserviamo quali sono i nomi di colonna;
# • Il dataset è bilanciato, ovvero, il numero di recensioni positive è uguale a quello delle negative, oppure no?

#dimesione righe e colonne 
n = amazon.shape

#sample 10 righe 
print(amazon.sample(10))

colonne = amazon.columns
print(colonne)

recensioni = amazon["Positive"] == 1
print(recensioni.count())
