import matplotlib.pyplot as plt
import geopandas as gpd

def geometricForm(Adress):
    form = gpd.read_file(f'/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS/{Adress}')
    form.plot(color = 'blue', edgecolor = 'white')
    plt.savefig("/home/mateus/Desktop/Backend sprint-3/img/geometric/geometricForm.png",format="png")
    return 