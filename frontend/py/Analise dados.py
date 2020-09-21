import matplotlib.pyplot as plt
import geopandas as gpd
#import shapefile

#sf = shapefile.Reader("/Desktop/AGENCIA_NACIONAL_AGUAS/AGENCIA_NACIONAL_AGUAS/geoft_bho_2017_curso_dagua.shp")
#sf.shapefileType


open("/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/drenagem/geoft_bho_2017_ponto_drenagem.dbf")

#menu
opção = 0
while opção != 5:
    print('''-------MENU-------\n~plotador de gráficos~\n[ 1 ] Curso dagua\n[ 2 ] Drenagem
[ 3 ] Nível\n[ 4 ] Todos os gráficos\n[ 5 ] Sair da aplicação''')
    opção = int(input("Qual sua opção: "))
    #gráfico curso dagua
    if opção == 1:
        curso = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/curso dagua")
        curso.plot(color = 'blue')
        plt.show()
    #grafico drenagem
    elif opção == 2:
        drenagem = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/drenagem")
        drenagem.plot(color = 'white', edgecolor='black')
        plt.show()
    #grafico nivel
    elif opção == 3:
        nivel = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/nivel")
        nivel.plot(color = 'white', edgecolor='green')
        plt.show()
    
    elif opção == 4:
        nivel = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/nivel")
        drenagem = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/drenagem")
        curso = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS teste/AGENCIA_NACIONAL_AGUAS/curso dagua")

        nivel.plot(color = 'white', edgecolor = 'green');drenagem.plot(color = 'white', edgecolor = 'black');curso.plot(color = 'blue', edgecolor = 'yellow')
        plt.show()

    
    else:
        print("ERRO: Opção invalida")
    

print("Fim da execução")


