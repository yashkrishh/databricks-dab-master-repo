# Databricks notebook source
# 1. Grab an initial parameter passed by the YAML
base_input = dbutils.widgets.get("t1_param")
print(f"Task 1 base parameter received: {base_input}")

# 2. Simulate some data transformation logic
updated_output = f"{base_input}-test"

# 3. Drop the package off at the Databricks Post Office!
dbutils.jobs.taskValues.set(key="from_t1", value=updated_output)
print(f"Task 1 successfully exported task value 'from_t1': {updated_output}")


print("Verifying Automated Pipeline Integration - Hello From GitHub Actions!")
print("Testing a completely clean push from our dedicated feature branch!")