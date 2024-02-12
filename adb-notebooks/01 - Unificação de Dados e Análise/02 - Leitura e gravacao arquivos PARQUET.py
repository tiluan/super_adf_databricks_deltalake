# Databricks notebook source
# DBTITLE 1,Criação de um dataframe com dados
#criando um dataframe com dados fixos
dados =[("Grimaldo ","Oliveira","Brasileira","Professor","M",3000),
("Ana ","Santos","Portuguesa","Atriz","F",4000),
("Roberto","Carlos","Brasileira","Analista","M",4000),
("Maria ","Santanna","Italiana","Dentista","F",6000),
("Jeane","Andrade","Portuguesa","Medica","F",7000)]
colunas=["Primeiro_Nome","Ultimo_nome","Nacionalidade","Trabalho","Genero","Salario"]
datafparquet=spark.createDataFrame(dados,colunas)
datafparquet.show()

# COMMAND ----------

# DBTITLE 1,Gravando o arquivo parquet
# datafparquet.write.parquet("/FileStore/tables/parquet/pessoal.parquet")

# COMMAND ----------

# DBTITLE 1,Subscrevendo o arquivo parquet
#Permite uma atualização do arquivo parquet
datafparquet.write.mode('overwrite').parquet('/FileStore/tables/parquet/pessoal.parquet')

# COMMAND ----------

# DBTITLE 1,Lendo o arquivo parquet e guardando em um dataframe
#Realizando uma atualização do arquivo parquet
datafleitura= spark.read.parquet("/FileStore/tables/parquet/pessoal.parquet")
datafleitura.show()

# COMMAND ----------

# DBTITLE 1,Realizando uma consulta SQL
#Criando uma consulta em SQL
datafleitura.createOrReplaceTempView("Tabela_Parquet")
ResultSQL = spark.sql("select * from Tabela_Parquet where salario >= 6000 ")
ResultSQL.show()

# COMMAND ----------

# DBTITLE 1,Particionando os dados do arquivo parquet em grupos
#Particionando os dados em um arquivo parquet
datafparquet.write.partitionBy("Nacionalidade","salario").mode("overwrite").parquet("/FileStore/tables/parquet/pessoal.parquet")

# COMMAND ----------

# DBTITLE 1,Exibindo os dados do parquet cuja a nacionalidade é brasileira
#Lendo o aquivo participonado do parquet
datafnacional=spark.read.parquet("/FileStore/tables/parquet/pessoal.parquet/Nacionalidade=Brasileira")
datafnacional.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Realizando uma pesquisa via SQL no arquivo parquet particionado
#Consultando diretamente o arquivo parquet particionado via SQL
spark.sql("CREATE OR REPLACE TEMPORARY VIEW Cidadao USING parquet OPTIONS (path \"/FileStore/tables/parquet/pessoal.parquet/Nacionalidade=Brasileira\")")
spark.sql("SELECT * FROM Cidadao where Ultimo_nome='Oliveira'").show()
