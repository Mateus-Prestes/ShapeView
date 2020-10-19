<div>
  <p align="center">
            <img src="https://user-images.githubusercontent.com/56441534/92442086-adf9e000-f185-11ea-8794-b6c5def3daf3.png" width = "39%">
            <img baackgroundcolor="white" width = "20%">
            <img src="https://user-images.githubusercontent.com/58118956/96368863-d97ccc80-112c-11eb-8a52-938b4327fc50.jpg" width = "39%"></p>
</div>     


# Sprint 2

Nesta sprint trouxemos o que na opnião de nosso time é de mais valor no momento para nosso cliente, sendo o corpo de nosso CRUD que tem a capacidade de se conectar com o banco de dados, e também o tratamento dos dados fornecidos pelo cliente, realizando o upload dos mesmos nas respectivas tabelas do banco. Estes serviços estão funcionando 100% separadamente, e nas proximas sprints entregaremos estes serviços integrados em uma só aplicação.

<p align="center">
  <img src="https://user-images.githubusercontent.com/56441534/96368958-5f991300-112d-11eb-8560-70bbdf57b9d6.jpeg"> </p>
 
# CRUD  

Ao entender o funcionamento do CRUD, começamos a trabalhar na etapa de estruturação do corpo do api, mais precisamente o backend. Assim, essa segunda etapa de desenvolvimento, nós focamos em entender a logica do programa para o funcionamento do CRUD, tal como a sua conexão com o servidor do banco de dados PostgreSQL.

Nesta etapa foi realizado o desenvolvimento de um aplicativo, que tem as funções de CREATE, READ, UPDATE e DELETE. Ele conta com uma conexão com o servidor do banco de dados do Postgre em localhost.

Esta aplicação foi desenvolvida com as seguintes tecnologias:
* Eclipse IDE 2020‑09
* Springboot 2.3.4
* Java 8
* PostgreSQL 13

## Funcionamento

![Screen Capture_select-area_20201004230547](https://user-images.githubusercontent.com/56441534/95036485-7c9a0480-069e-11eb-9169-d35b721ca85a.gif)

# Upload dos shapefile's nas respectivas tabelas do Banco de Dados

## Upload na tabela "ft_bacia_hidrografia_n1"

Nessa etapa da aplicação, ela fará a importação das bibliotecas utilizadas  em seu funcionamento. Em seguida ela faz a conexão com o banco de dados. Assim a aplicação também atribui os dados geograficos referentes a FT_BACIA_HIDROGRÁFICA_N1 a uma variável. Os dados são tratados e logo após são enviados as sua respectiva tabela e inseridas no banco de dados.

![Bacia Hidrografica n1](https://user-images.githubusercontent.com/56441534/96370050-fa482080-1132-11eb-9f05-7e4c02b10077.gif)

## Upload na tabela "ft_curso_dagua"

Seguindo a mesma lógica da etapa anterior temos agora os dados referentes a FT_CURSO_DAGUA.

![Curso dagua](https://user-images.githubusercontent.com/56441534/96370162-4f843200-1133-11eb-861e-91c429bb1476.gif)

## Upload na tabela "ft_ponto_drenagem"

Seguindo a mesma lógica da etapa anterior temos agora os dados referentes a FT_PONTO_DRENAGEM.

![Ponto drenagem](https://user-images.githubusercontent.com/56441534/96370220-79d5ef80-1133-11eb-8f81-1d473d33d64e.gif)

# Gráfico BurnDown

Nosso gráfico BurnDown representando nosso trabalho ao longo do desenvolvimento da Sprin-2.

![BurnDown-Sprint-2](https://user-images.githubusercontent.com/56441534/96372780-f28e7900-113e-11eb-8dad-404c83ced5f2.png)


