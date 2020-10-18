import geopandas as gpd
import postgresql
import psycopg2


try:
    con = psycopg2.connect(host ='127.0.0.1',port = '5432', database ='DB_PI3',
    user='postgres', password ='8920,')
    cur = con.cursor()

    # Print PostgreSQL Connection properties
    print(con.get_dsn_parameters(),"\n") 

    # # Print PostgreSQL version
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record,"\n")
    
except (Exception, psycopg2.Error) as error: 
    print("Error while connecting to PostgreSQL", error)

FT_PONTO_DRENAGEM = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS__/FT_PONTO_DRENAGEM")

##CÓDIGO ÚNICO DO PONTO DE DRENAGEM
idponto = []
##CÓDIGO DO CURSO D'ÁGUA
cocursodag = []
##DESCRIÇÃO DO PONTO
deponto = []
##GEOMETRIA DO DADO (POLÍGONO) EM SISTEMA DE COORDENADAS GEOGRÁFICAS EPSG:4674
geometry = []

for f in FT_PONTO_DRENAGEM['idponto']:
    idponto.append(f)
for g in FT_PONTO_DRENAGEM['cocursodag']:
    cocursodag.append(g)
for h in FT_PONTO_DRENAGEM['deponto']:
    deponto.append(h)
for i in FT_PONTO_DRENAGEM['geometry']:
    geometry.append(i)

c = 0
for i in range(0, len(idponto)):
    sql = (f"insert into ft_ponto_drenagem (pdr_cd, pdr_cd_curso_dagua, pdr_ds, geom) values ('{idponto[c]}','{cocursodag[c]}','{deponto[c]}','{geometry[c]}')")
    cur.execute(sql)
    con.commit()
    count = cur.rowcount
    print (count,"Record inserted successfully into the table ft_ponto_drenagem")
    c+=1
