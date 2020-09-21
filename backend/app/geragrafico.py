import matplotlib.pyplot as plt
import geopandas as gpd
import postgresql


def grafico():
    curso_dagua = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/curso dagua")

    curso_dagua.plot(color = 'blue', edgecolor = 'yellow')
    plt.savefig("frontend/imagem/grafico/teste.png",format="png")
    return 