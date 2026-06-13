# Databricks notebook source
# 1. Snatch the package that the YAML intercepted from Task 1
shared_runtime_value = dbutils.widgets.get("from_t1_resolved")

print(f"Task 2 successfully intercepted shared data from Task 1: {shared_runtime_value}")