# Databricks notebook source
# DBTITLE 1,Script 1
# MAGIC %r
# MAGIC
# MAGIC library(ggplot2)
# MAGIC ggplot(data = CO2) +
# MAGIC geom_point(mapping = aes(x = conc, y = uptake))

# COMMAND ----------

# DBTITLE 1,Script 2
# MAGIC %r
# MAGIC #Mapa de Bolhas
# MAGIC # Libraries
# MAGIC install.packages("gridExtra")
# MAGIC library(ggplot2)
# MAGIC library(dplyr)
# MAGIC # carga dos dados
# MAGIC install.packages("gapminder")
# MAGIC library(gapminder)
# MAGIC data <- gapminder %>% filter(year=="2007") %>% dplyr::select(-year)
# MAGIC # Exibição do gráfico
# MAGIC data %>%
# MAGIC arrange(desc(pop)) %>%
# MAGIC mutate(country = factor(country, country)) %>%
# MAGIC ggplot(aes(x=gdpPercap, y=lifeExp, size=pop, color=continent)) +
# MAGIC geom_point(alpha=0.7) +
# MAGIC scale_size(range = c(.5, 24), name="População (M)") +
# MAGIC labs(x = "Valor per Capta", y = "Expectativa Vida")

# COMMAND ----------

# DBTITLE 1,Script 3
# MAGIC %r
# MAGIC library(ggplot2)
# MAGIC # base interna mtcars - Violino
# MAGIC dados <- ggplot(mtcars, aes(factor(cyl), mpg))
# MAGIC dados + geom_violin()
