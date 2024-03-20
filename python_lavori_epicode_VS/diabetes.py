import pandas as pd 


path_dataset = "C:/Users/HOME/Desktop/python_lavori_epicode_VS/beginner_datasets/" 
file = "diabetes.csv"
path = path_dataset + file

#Osserviamone le dimensioni e un'anteprima di cinque righe; • Prendiamoci un po' di tempo per dare un'occhiata ai metadati delle colonne; 
#• Stampiamo dei descrittori statistici del dataset; • Selezioniamo i dati relativi a diverse fasce di età: <20, 20-30, 30-40, 40-50, >50; 
#• Qual è la media della pressione sanguigna diastolica per le diverse fasce di età? • Qual è la media della pressione per ogni singolo anno di età?
diabetes = pd.read_csv(path)

# tupla righe e colonne 
n = diabetes.shape 

#sample di 10 righe 
print(diabetes.sample(10), n)

# statistica delle colonne 
colonne = diabetes.columns
descrizione = diabetes.describe()

#filtri eta 
min_20 = diabetes["Age (years)"] < 20
y_20_30 =  (diabetes["Age (years)"] >= 20) & (diabetes["Age (years)"] <= 30) 
y_30_40 =  (diabetes["Age (years)"] >= 30) & (diabetes["Age (years)"] <= 40) 

diabetes_30_40 = diabetes[y_30_40]

# per ogni fascia di età basta usare il prorpio dataframe 
avg_pressione_30_40 = diabetes_30_40["Diastolic blood pressure (mm Hg)"].mean()
print(avg_pressione_30_40)

print(diabetes.columns)

# raggurppo per age e faccio media età 
avg_singolo_anno = diabetes.groupby("Age (years)").mean()
print(avg_singolo_anno)