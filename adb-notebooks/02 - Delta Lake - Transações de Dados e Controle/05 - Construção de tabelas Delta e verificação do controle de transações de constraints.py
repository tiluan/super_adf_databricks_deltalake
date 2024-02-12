# Databricks notebook source
# MAGIC %md
# MAGIC ## Criação das tabelas TB_AUTOR,TB_LIVRO e a associativa TB_LIVRO_AUTOR

# COMMAND ----------

# MAGIC %scala
# MAGIC val Tscrisql = "CREATE OR REPLACE TABLE TB_AUTOR (ID_AUTOR DOUBLE,NOME STRING,SEXO STRING,DATA_NASCIMENTO STRING) USING DELTA ;"
# MAGIC spark.sql(Tscrisql);
# MAGIC
# MAGIC val Tscrisql1 = "CREATE OR REPLACE TABLE TB_LIVRO (ID_LIVRO DOUBLE,ISBN STRING,TITULO STRING,EDICAO DOUBLE,PRECO DOUBLE,QTDE_ESTOQUE DOUBLE) USING DELTA;"
# MAGIC spark.sql(Tscrisql1);
# MAGIC
# MAGIC val Tscrisql3 = "CREATE OR REPLACE TABLE TB_LIVRO_AUTOR (ID_LIVRO_AUTOR DOUBLE,ID_LIVRO DOUBLE,ID_AUTOR DOUBLE) USING DELTA;"
# MAGIC spark.sql(Tscrisql3);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Inserção de registros na tabela TB_AUTOR

# COMMAND ----------

# MAGIC %scala
# MAGIC val scrisql = "Insert into TB_AUTOR (ID_AUTOR,NOME,SEXO,DATA_NASCIMENTO) values (1,'Joao','M', '01/01/1970');"
# MAGIC spark.sql(scrisql);
# MAGIC
# MAGIC val scrisql1 = "Insert into TB_AUTOR (ID_AUTOR,NOME,SEXO,DATA_NASCIMENTO) values (2,'Maria','F', '25/11/1975');"
# MAGIC spark.sql(scrisql1);
# MAGIC
# MAGIC val scrisql2 = "Insert into TB_AUTOR (ID_AUTOR,NOME,SEXO,DATA_NASCIMENTO) values (3,'Sandra','F', '14/11/1978');"
# MAGIC spark.sql(scrisql2);
# MAGIC
# MAGIC val scrisql3 = "Insert into TB_AUTOR (ID_AUTOR,NOME,SEXO,DATA_NASCIMENTO) values (4,'Tereza','F', '21/11/1978');"
# MAGIC spark.sql(scrisql3);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Inserção de registros na tabela TB_LIVRO

# COMMAND ----------

# MAGIC %scala
# MAGIC val Lscrisql = "Insert into TB_LIVRO (ID_LIVRO,ISBN,TITULO,EDICAO,PRECO,QTDE_ESTOQUE) values (1,'1234567890','Banco de Dados',2,10,407);"
# MAGIC spark.sql(Lscrisql);
# MAGIC
# MAGIC val Lscrisql1 = "Insert into TB_LIVRO (ID_LIVRO,ISBN,TITULO,EDICAO,PRECO,QTDE_ESTOQUE) values (2,'2345678901','Redes de Computadores',1,10,60);"
# MAGIC spark.sql(Lscrisql1);
# MAGIC
# MAGIC val Lscrisql2 = "Insert into TB_LIVRO (ID_LIVRO,ISBN,TITULO,EDICAO,PRECO,QTDE_ESTOQUE) values (3,'3456789012','Interface Homem-Maquina',3,10,10);"
# MAGIC spark.sql(Lscrisql2);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Inserção de registros na tabela TB_LIVRO_AUTOR

# COMMAND ----------

# MAGIC %scala
# MAGIC val LAscrisql = "Insert into TB_LIVRO_AUTOR (ID_LIVRO_AUTOR,ID_LIVRO,ID_AUTOR) values (1,1,1);"
# MAGIC spark.sql(LAscrisql);
# MAGIC
# MAGIC val LAscrisql1 = "Insert into TB_LIVRO_AUTOR (ID_LIVRO_AUTOR,ID_LIVRO,ID_AUTOR) values (2,1,2);"
# MAGIC spark.sql(LAscrisql1);
# MAGIC
# MAGIC val LAscrisql2 = "Insert into TB_LIVRO_AUTOR (ID_LIVRO_AUTOR,ID_LIVRO,ID_AUTOR) values (3,2,3);"
# MAGIC spark.sql(LAscrisql2);
# MAGIC
# MAGIC val LAscrisql3 = "Insert into TB_LIVRO_AUTOR (ID_LIVRO_AUTOR,ID_LIVRO,ID_AUTOR) values (4,3,2);"
# MAGIC spark.sql(LAscrisql3);
# MAGIC
# MAGIC val LAscrisql4 = "Insert into TB_LIVRO_AUTOR (ID_LIVRO_AUTOR,ID_LIVRO,ID_AUTOR) values (5,3,3);"
# MAGIC spark.sql(LAscrisql4);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Selecionando os registros, ligando todas as tabelas

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT TB_LIVRO.TITULO, TB_LIVRO.ISBN,TB_LIVRO.PRECO,TB_AUTOR.NOME,TB_AUTOR.DATA_NASCIMENTO FROM TB_LIVRO
# MAGIC INNER JOIN TB_LIVRO_AUTOR ON TB_LIVRO.ID_LIVRO = TB_LIVRO_AUTOR.ID_LIVRO
# MAGIC INNER JOIN TB_AUTOR ON TB_AUTOR.ID_AUTOR = TB_LIVRO_AUTOR.ID_AUTOR

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criando uma check constraints para a tabela TB_AUTOR, somente permitindo a inserção de 4 registros

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE TB_AUTOR DROP CONSTRAINT IF EXISTS validIds;
# MAGIC ALTER TABLE TB_AUTOR ADD CONSTRAINT validIds CHECK (ID_AUTOR > 0 AND ID_AUTOR < 5);
# MAGIC SHOW TBLPROPERTIES TB_AUTOR;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verificando se a check constraints irá funcionar, executando um insert

# COMMAND ----------

# MAGIC %scala
# MAGIC val scrisql = "Insert into TB_AUTOR (ID_AUTOR,NOME,SEXO,DATA_NASCIMENTO) values (5,'Joao','M', '01/01/1970');"
# MAGIC spark.sql(scrisql);
