import matplotlib.pyplot as plt
import geopandas as gpd
import postgresql

curso = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/curso dagua")
drenagem = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/drenagem")
nivel = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/nivel")

print(curso.info())
print(drenagem.info())
print(nivel.info())

print(curso.head())
print(drenagem.head())
print(nivel.head())

nivel.plot(color = 'white', edgecolor = 'green');drenagem.plot(color = 'white', edgecolor = 'black');curso.plot(color = 'blue', edgecolor = 'yellow')
#plt.show()