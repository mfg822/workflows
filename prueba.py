import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car_data.csv')
df.head()

# Agrupa por compañía y cuenta el número de ventas
sales_by_company = df.groupby('Company')['Car_id'].count()

# Crea un histograma
plt.bar(sales_by_company.index, sales_by_company.values)
plt.xlabel('Compañía')
plt.ylabel('Número de Ventas')
plt.xticks(rotation=90)
plt.title('Número de Ventas de Coches por Compañía')
plt.show()