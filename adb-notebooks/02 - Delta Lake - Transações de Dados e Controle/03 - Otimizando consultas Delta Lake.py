# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS hotel;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Carregando de arquivos Parquet sobre dados de hotel
# MAGIC CREATE TABLE hotel
# MAGIC USING parquet
# MAGIC PARTITIONED BY (Categoria)
# MAGIC SELECT _c0 as Ordem, _c1 as Tipo, _c2 as Situacao, _c3 as Tip_local, _c4 as Categoria, _c5 as Tip_Local2, _c6 as Tip_local3, _c7 as Acomodacao, _c8 as Cidade, _c9 as Pais, _c10 as Endereco, _c11 as Latitude, _c12 as Longitude, _c13 as Provincia, _c14 as CEP, _c15 as UF, _c16 as Data_estadia, _c17 as Revisao_texto, _c17 as Revisao_titulo, _c19 as Revisao_cidade, _c20 as Endereco_web, _c21 as Comentario_usuario, _c22 as Resumo, _c23 as Comentario2, _c24 as Comentario3, _c25 as Comentario4
# MAGIC FROM csv.`dbfs:/FileStore/tables/hotel/Datafiniti_Hotel_Reviews_Jun19.csv`

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Fazendo uma contagem das principais categorias e comentarios
# MAGIC SELECT Categoria,Comentario2,Comentario3,count(*) as Total
# MAGIC FROM hotel
# MAGIC GROUP BY Categoria,Comentario2,Comentario3
# MAGIC ORDER BY Categoria,Total DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Criando a tabela Delta
# MAGIC DROP TABLE IF EXISTS hotel;
# MAGIC
# MAGIC CREATE TABLE hotel
# MAGIC USING delta
# MAGIC PARTITIONED BY (categoria)
# MAGIC SELECT _c0 as Ordem, _c1 as Tipo, _c2 as Situacao, _c3 as Tip_local, _c4 as Categoria, _c5 as Tip_Local2, _c6 as Tip_local3, _c7 as Acomodacao, _c8 as Cidade, _c9 as Pais, _c10 as Endereco, _c11 as Latitude, _c12 as Longitude, _c13 as Provincia, _c14 as CEP, _c15 as UF, _c16 as Data_estadia, _c17 as Revisao_texto, _c17 as Revisao_titulo, _c19 as Revisao_cidade, _c20 as Endereco_web, _c21 as Comentario_usuario, _c22 as Resumo, _c23 as Comentario2, _c24 as Comentario3, _c25 as Comentario4
# MAGIC FROM csv.`dbfs:/FileStore/tables/hotel/Datafiniti_Hotel_Reviews_Jun19.csv`

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Otimizando a consulta da tabela Delta com o campo Pais, é importante que busque o campo que melhor otimiza
# MAGIC OPTIMIZE hotel ZORDER BY (Pais);

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Executando a consulta otimizada na tabela Delta
# MAGIC SELECT Categoria,Comentario2,Comentario3,count(*) as Total
# MAGIC FROM hotel
# MAGIC GROUP BY Categoria,Comentario2,Comentario3
# MAGIC ORDER BY Categoria,Total DESC;
