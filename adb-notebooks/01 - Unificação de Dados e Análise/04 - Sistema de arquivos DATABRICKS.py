# Databricks notebook source
# DBTITLE 1,Acessando o help de comando
# MAGIC %fs help

# COMMAND ----------

# DBTITLE 1,Listando as pastas
# MAGIC %fs ls /

# COMMAND ----------

# DBTITLE 1,Listando as pastas
dbutils.fs.ls("/")

# COMMAND ----------

# DBTITLE 1,Criando as pastas (exemplo, criando a pasta vendas)
# MAGIC %fs mkdirs vendas

# COMMAND ----------

# DBTITLE 1,Mostrando a pasta criada (exemplo, a pasta vendas)
# MAGIC %fs ls /FileStore/

# COMMAND ----------

# DBTITLE 1,Copiando um arquivo de uma pasta para outra
# MAGIC %fs cp /FileStore/tables/carga/vinhos_no_mundo.csv /FileStore/vendas2/copia_vinhos.csv

# COMMAND ----------

# DBTITLE 1,Copiando um arquivo de uma pasta para outra
dbutils.fs.cp("/FileStore/tables/carga/vinhos_no_mundo.csv", "/FileStore/vendas3/copia2_vinhos.csv")

# COMMAND ----------

# DBTITLE 1,Renomeando (troca de nome) de um arquivo
# MAGIC %fs mv /FileStore/vendas2/copia_vinhos.csv /FileStore/vendas2/copia_muda_vinhos.csv

# COMMAND ----------

# DBTITLE 1,Renomeando (troca de nome) de um arquivo
dbutils.fs.mv("/FileStore/vendas2/copia_muda_vinhos.csv", "/FileStore/vendas2/copia_troca_vinhos.csv")

# COMMAND ----------

# DBTITLE 1,Elimina um arquivo
# MAGIC %fs rm /FileStore/vendas2/copia_troca_vinhos.csv

# COMMAND ----------

# DBTITLE 1,Elimina um arquivo
# MAGIC %fs rm /FileStore/vendas3/copia2_vinhos.csv
# MAGIC ou
# MAGIC dbutils.fs.rm("/FileStore/vendas3/copia2_vinhos.csv")

# COMMAND ----------

# DBTITLE 1,Elimina a pasta
# MAGIC %fs rm -r /FileStore/vendas2/
# MAGIC Ou
# MAGIC dbutils.fs.rm("/FileStore/vendas2/", recurse=True)

# COMMAND ----------

# DBTITLE 1,Realizando uma pesquisa em bash-linux
# MAGIC %%bash
# MAGIC find /databricks -name "*.csv" | grep "fa"
