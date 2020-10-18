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

FT_CURSO_DAGUA = gpd.read_file("/home/mateus/Desktop/AGENCIA_NACIONAL_AGUAS__/FT_CURSO_DAGUA")

##CÓDIGO ÚNICO DO CURSO D'ÁGUA
idcda = []
##CÓDIGO OTTO PFAFSTETTER
cocursodag = []
##DISTÂNCIA, EM QUILÔMETROS, DA FOZ DO CURSO D'ÁGUA DE REFERÊNCIA ATÉ A LINHA DE COSTA
nudistbacc = []
##COMPRIMENTO DO CURSO D'ÁGUA, EM QUILÔMETROS
nucompcda = []
##ÁREA DA BACIA REFERENTE AO CURSO D'ÁGUA
nuareabacc = []
##CÓDIGO DO CURSO D'ÁGUA ONDE DESAGUA
cocdadesag = []
##NÍVEL DE OTTO PFAFSTETTER DO CURSO D'ÁGUA
nunivotcda = []
##ORDEM DO CURSO D'ÁGUA
nuordemcda = []
##DOMINIALIDADE
dedominial = []
##GEOMETRIA DO DADO (LINHA) EM SISTEMA DE COORDENADAS GEOGRÁFICAS EPSG:4674
geometry = []

for f in FT_CURSO_DAGUA['idcda']:
    idcda.append(f)
for g in FT_CURSO_DAGUA['cocursodag']:
    cocursodag.append(g)
for h in FT_CURSO_DAGUA['nudistbacc']:
    nudistbacc.append(h)
for i in FT_CURSO_DAGUA['nucompcda']:
    nucompcda.append(i)
for j in FT_CURSO_DAGUA['nuareabacc']:
    nuareabacc.append(j)
for k in FT_CURSO_DAGUA['cocdadesag']:
    cocdadesag.append(k)
for l in FT_CURSO_DAGUA['nunivotcda']:
    nunivotcda.append(l)
for m in FT_CURSO_DAGUA['nuordemcda']:
    nuordemcda.append(m)
for n in FT_CURSO_DAGUA['geometry']:
    dedominial.append(n)
for o in FT_CURSO_DAGUA['geometry']:
    geometry.append(o)

c = 0
for i in range(0, len(idcda)):
    sql = (f'''insert into ft_curso_dagua (cda_cd, cda_cd_otto, cda_nu_dist_bh, cda_nu_comp,
    cda_ar_bacia, cda_cd_desagua, cda_nu_nivel_otto, cda_nu_ordem, cda_ds_dominialidadE, geom) values
    ('{idcda[c]}','{cocursodag[c]}','{nudistbacc[c]}','{nucompcda[c]}','{nuareabacc[c]}',
        '{cocdadesag[c]}','{nunivotcda[c]}', '{nuordemcda[c]}','{dedominial[c]}','{geometry[c]}')''')
    cur.execute(sql)
    con.commit()
    count = cur.rowcount
    print (count,"Record inserted successfully into the table ft_curso_dagua")
    c+=1
