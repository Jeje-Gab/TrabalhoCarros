from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(io.StringIO(uploaded['CarrosVendidos.csv'].decode('utf-8')),encoding='ISO-8859-1')
df

xEixo = 'Marca'
yEixo = 'Quantidade Vendida'

fig, ax = plt.subplots(figsize=(8,6))
nameFig = 'graficoItem.png'

marcas = df["Carro"]
vendas = df["Qtd Vendas"]

ax.plot(marcas,vendas,marker = 'o', lw= 2, ls ='-', ms = 10, color = 'y')

ax.set_xlabel(xEixo, fontsize= 22)
ax.set_ylabel(yEixo, fontsize= 22)
ax.tick_params(labelsize=16, labelrotation = 30)
#ax.grid(color ="black")

ax.grid(which='minor', alpha=0.1, color ='red')
ax.grid(which='major', alpha=0.7, color ='red')

####

fig.savefig('grafico.png')
plt.show()


