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

FT_BACIA_HIDROGRAFICA_N1 = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS__/FT_BACIA_HIDROGRAFICA_N1")

##CÓDIGO ÚNICO DA BACIA HIDROGRÁFICA
wts_pk = []
##CÓDIGO OTTO PFAFSTETTER
wts_cd_pfa = []
##ÁREA DA BACIA HIDROGRÁFICA
wts_gm_are = []
##GEOMETRIA DO DADO (POLÍGONO) EM SISTEMA DE COORDENADAS GEOGRÁFICAS EPSG:4674
geometry = []

for f in FT_BACIA_HIDROGRAFICA_N1['wts_pk']:
    wts_pk.append(f)
for g in FT_BACIA_HIDROGRAFICA_N1['wts_cd_pfa']:
    wts_cd_pfa.append(g)
for h in FT_BACIA_HIDROGRAFICA_N1['wts_gm_are']:
    wts_gm_are.append(h)
for i in FT_BACIA_HIDROGRAFICA_N1['geometry']:
    geometry.append(i)

c = 0
for i in range(0, len(wts_pk)):
    sql = (f"insert into ft_bacia_hidrografica_n1 (bhi_cd, bhi_cd_otto, bhi_ar, geom) values ('{wts_pk[c]}','{wts_cd_pfa[c]}','{wts_gm_are[c]}','{geometry[c]}')")
    cur.execute(sql)
    con.commit()
    count = cur.rowcount
    print (count,"Record inserted successfully into the table ft_bacia_hidrografica_n1")
    c+=1
















                                