# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Visão Geral - Importação de arquivo
# MAGIC
# MAGIC Este notebook mostrará como criar e consultar uma tabela ou DataFrame que você carregou no DBFS. [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) é um sistema de arquivos Databricks que permite armazenar dados para consulta dentro do Databricks. Este notebook pressupõe que você já tenha um arquivo dentro do DBFS do qual gostaria de ler..
# MAGIC
# MAGIC Este notebook foi escrito em **Python** portanto o tipo de célula padrão é Python. No entanto, você pode usar idiomas diferentes usando a sintaxe `%LANGUAGE` syntax. Python, Scala, SQL e R são todos suportados.

# COMMAND ----------

# Localização e tipo de arquivo
file_location = "/FileStore/tables/cliente/clientes.json"
file_type = "json"

# Opções do CSV
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# As opções aplicadas são para arquivos CSV. Para outros tipos de arquivo, estes serão ignorados.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

# Criar uma visualização ou tabela

temp_table_name = "clientes_json"

df.createOrReplaceTempView(temp_table_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Consulta a tabela temporária criada em uma célula SQL */
# MAGIC
# MAGIC select * from `clientes_json`

# COMMAND ----------

# Com isso registrado como visualização temporária, ele estará disponível apenas para este notebook específico. Se quiser que outros usuários possam consultar esta tabela, você também pode criar uma tabela a partir do DataFrame.
# Depois de salva, esta tabela persistirá nas reinicializações do cluster, bem como permitirá que vários usuários em diferentes notebooks consultem esses dados.
# Para fazer isso, escolha o nome da sua tabela e remova o comentário da linha inferior.

permanent_table_name = "clientes_json"

# df.write.format("parquet").saveAsTable(permanent_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC #######Primeiro Script , trabalhando com carga de dados e ajuste de registros no Delta Lake
# MAGIC ##Carrega os dados do arquivo Json

# COMMAND ----------

df.createOrReplaceTempView("clientes_json");
saida =spark.sql("SELECT * FROM clientes_json")
saida.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Carrega os dados no Delta Lake gerando uma tabela chamada compras, note USING DELTA

# COMMAND ----------

# MAGIC %scala
# MAGIC val scrisql = "CREATE OR REPLACE TABLE compras (id STRING, date_order STRING,customer STRING,product STRING,unit INTEGER,price DOUBLE) USING DELTA PARTITIONED BY (date_order) ";
# MAGIC spark.sql(scrisql);

# COMMAND ----------

# MAGIC %md
# MAGIC ##Lista os dados do Delta Lake, que estará vazia

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.sql("select * from compras").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Criando um merge para carregar os dados da tabela temporário no Delta Lake

# COMMAND ----------

# MAGIC %scala
# MAGIC val mergedados = "Merge into compras " +
# MAGIC "using clientes_json as cmp_view " +
# MAGIC "ON compras.id = cmp_view.id " +
# MAGIC "WHEN MATCHED THEN " +
# MAGIC "UPDATE SET compras.product = cmp_view.product," +
# MAGIC "compras.price = cmp_view.price " +
# MAGIC "WHEN NOT MATCHED THEN INSERT * ";
# MAGIC spark.sql(mergedados);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exibe os dados que foram carregados com o merge

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.sql("select * from compras").show();

# COMMAND ----------

# MAGIC %md
# MAGIC ##Atualiza os dados do id=4 com o comando update

# COMMAND ----------

# MAGIC %scala
# MAGIC val atualiza_dados = "update compras " +
# MAGIC "set product = 'Geladeira' " +
# MAGIC "where id =4";
# MAGIC spark.sql(atualiza_dados);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exibe os dados que foram carregados, note a atualização no id=4

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.sql("select * from compras").show();

# COMMAND ----------

# MAGIC %md
# MAGIC ## Eliminação do registro cujo o id=4

# COMMAND ----------

# MAGIC %scala
# MAGIC val deletaregistro = "delete from compras where id = 1";
# MAGIC spark.sql(deletaregistro);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exibe os dados que foram carregados

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.sql("select * from compras").show();
