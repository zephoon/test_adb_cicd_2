# Databricks notebook source

# COMMAND ----------

# Restart Python after installing the Python wheel.
dbutils.library.restartPython()

# COMMAND ----------

from dabdemo.add_one import add_one


2 = add_one()

print(2)

