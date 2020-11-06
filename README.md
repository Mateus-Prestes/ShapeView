<div>
  <p align="center">
            <img src="https://user-images.githubusercontent.com/56441534/92442086-adf9e000-f185-11ea-8794-b6c5def3daf3.png" width = "39%">
            <img baackgroundcolor="white" width = "20%">
            <img src="https://user-images.githubusercontent.com/58118956/96368863-d97ccc80-112c-11eb-8a52-938b4327fc50.jpg" width = "39%"></p>
</div>    

# Projeto Integrador - Fatec São José dos Campos - 3º Semestre

Projeto Integrador realizado por alunos e professores do terceiro semestre de Análise e Desenvolvimento de Sistemas em Fatec São José dos Campos - Prof. Jessen Vidal, e uma empresa especializada em tecnologia espacial. Projeto esse realizado através de metodologia SCRUM com intuito de que nós alunos tenhamos um contato real com uma empresa e apresentemos soluções frente aos seus problemas.

## Professores Orientadores
* ### Prof. Me. Giuliano Araujo Bertoti
* ### Prof. Me. José Walmir Gonçalves Duque
* ### Prof. Me. Gerson da Penha Neto
* ### Prof. Claudio Etelvino de Lima

## Time

* ### Lucas Hiroaki Okazaki – P.O/Dev Team
* ### Mateus Prestes Teodoro Alves– Scrum Master/Dev Team
* ### Fabrício Rodrigues de Oliveira– Dev Team
* ### João Vitor de Oliveira Soeiro – Dev Team
* ### Rodrigo Félix da Silva – Dev Team
* ### William Daisuke Honda – Dev Team
* ### Kleber Apolinário Júnior - Dev Team
* ### João Pedro Apse Paes - Dev Team


## Objetivo

O projeto tem como principal objetivo o desenvolvimento de uma aplicação web, que funcione como uma ETL para extrair dados de arquivos de formatos Shapefile e carrega-los em um banco de dados geográficos, fazendo também o processo inverso.

## Shapefile

Shapefile é um formato de arquivo que contém dados geoespaciais salvos em forma de vetor. Descrevem geometrias: pontos, linhas, e polígonos. Entre outros, essas mesmas geometrias podem respectivamente representar Poços, Rios, e Lagos. Cada geometria podendo ter atributos que as descrevem, por exemplo: nome, temperatura ou profundidade.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98367989-52c55c00-2015-11eb-85e9-f688d5b67298.png"> </p>

## O que é uma ETL

Dentro do contexto de Data Warehouse (DW) e Business Intelligence (BI), o processo de ETL é muito popular. A sigla tem, por sua vez, como significado Extração, Transformação e Carga (Extract, Transform and Load) e trata da sistematização do tratamento e limpeza dos dados oriundos dos diversos sistemas organizacionais (OLTP) para a inserção em um Data Warehouse ou Data Mart.

Como podemos perceber, esse processo possui três etapas. A primeira delas é a Extração, a segunda a Transformação e por fim, a terceira etapa de Carga. Cada uma delas com grande importância para o que tenhamos sucesso na transição dos dados do sistema para a origem do DW.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98368865-c87df780-2016-11eb-91de-7a5d85114f05.png"> </p>

A etapa de extração pode ser entendida como a fase em que os dados são extraídos dos OLTPs e conduzidos para a staging area (área de transição ou área temporária), onde são convertidos para um único formato. A conversão se faz necessária devido a heterogeneidade existente nas informações oriundas desses sistemas, sendo essencial a conformação prévia para o tratamento adequado.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98369016-03802b00-2017-11eb-9ccc-dad11051c2ef.png"> </p>
  
Após a extração, teremos subsídios para iniciar a etapa de transformação e limpeza dos dados. Nessa fase são corrigidos, padronizados e tratados os desvios e inconsistências, transformando os dados de acordo com as regras do negócio.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98369449-be102d80-2017-11eb-8abf-4ebcd8f7c209.png"> </p>

A etapa de carga ocorre em sequência com a de transformação. Assim que são efetuados os tratamentos necessários nos dados, a carga no DW é iniciada. Essa fase se resume a persistência dos dados na base consolidada.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98369518-d718de80-2017-11eb-814f-ddede1d5aeb6.png"> </p>

O ETL é fundamental para qualquer iniciativa de DW. Porém deve ser planejado com cuidado para não comprometer os sistemas transacionais (OLTP) das empresas. Um bom ETL deve ter escalabilidade e ser manutenível.

Portanto, devemos tratar o ETL como sendo o “cordão umbilical” que une e possibilita a condução dos dados ao DW. O processo deve ser bem planejado para evitar transtornos futuros e até mesmo para que não ocasione, em casos extremos, a interrupção dos sistemas operacionais da empresa. Dessa forma, o DW terá informações tratadas, com qualidade e grande valor para apoiar as decisões organizacionais.

Com esse entendimento do processo, surgiu o ShapView. A ferramenta de desenvolvida pela equipe.

# ShapView - Seu ShapeFile rápido e fácil

<p align="center">
  <img src="https://user-images.githubusercontent.com/56441534/94135974-9768af80-fe3a-11ea-85c4-e640cd767dbb.jpeg"> </p>

O ShapView nasceu com o propósito de ser uma ferramenta funcional e intuitiva com um sistema ETL. Sendo capaz de realizar os processos de um ETL com os dados em formato Shapefile, salvando os registros em um banco de dados geográficos. Além de ter, também, a funcionalidade de converter os dados do banco de volta em um formato Shapefile , tendo como partida os dados posteriormente registrados no banco.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/98375738-4d6e0e80-2021-11eb-9e9e-4c84a1acce36.png"> </p>

##  Requisitos Funcionais

* Carregamento de dados geográficos (ponto, linha e polígono) e seus atributos, em tabelas existentes do seu respectivo banco de dados geográficos.
* Recuperação de dados geográficos (ponto, linha e polígono) e seus atributos, dados esses que estão armazenados em seu respectivo banco de dados geográficos.

## Requisitos não funcionais

* Linguagem Java;
* Banco de Dados Geográficos PostGIS;
* Documentações.

## Tecnologias utilizadas para desenvolvimento da Aplicação.

Essa aplicação conta com a utilização de diversas tecnologias para o seu desenvolvimento. Para o desenvolvimento do Frontend da aplicação foram utilizadas as tecnologias:

<p align="left">
  <img src="https://user-images.githubusercontent.com/58118956/98377565-bd7d9400-2023-11eb-88fb-55ca1564dfe5.png"> </p>


Para o desenvolvimento do Backend da aplicação foram utilizadas as tecnologias:

<p align="left">
  <img src="https://user-images.githubusercontent.com/58118956/98378720-287b9a80-2025-11eb-81af-8abb515c14b8.png"> </p>
  
Como foi necessário a utilização de um banco de dados, a equipe utilizou o PostGre/Gis

<p align="left">
  <img src="https://user-images.githubusercontent.com/58118956/98378973-7db7ac00-2025-11eb-9bdf-50e799a76ba2.png"> </p>

## BackLog
 A equipe, juntamente com os colaboradores, definiu um Backlog a ser seguido para apresentar os resultados que foram alcançados de acordo com a data de entrega de cada etapa de desenvolvimento. Segue modelo do Backlog da equipe.

<p align="center">
  <img src="https://user-images.githubusercontent.com/58118956/96376895-fb3f7900-1157-11eb-8eaa-e6fe8399f054.jpeg"> </p>

## Etapas de Desenvolvimento

O desenvolvimento da ferramenta será divido em etapas denominadas Sprints, onde a equipe apresentara os avanços no desenvolvimento para a empresa em datas específicas.

<a href='https://github.com/Mateus-Prestes/Projeto-integrador-3-Semestre/tree/sprint-1'> Sprint 1 </a> - 20/09/2020

<a href='https://github.com/Mateus-Prestes/Projeto-integrador-3-Semestre/tree/sprint-2'> Sprint 2 </a> - 18/10/2020

<a href='https://github.com/Mateus-Prestes/Projeto-integrador-3-Semestre/tree/sprint-3'> Sprint 3 </a> - 08/11/2020

<a href='https://github.com/Mateus-Prestes/Projeto-integrador-3-Semestre/tree/sprint-4'> Sprint 4 </a> - 29/11/2020
