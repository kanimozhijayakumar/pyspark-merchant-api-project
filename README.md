# PySpark Merchant API Data Pipeline

## 📌 Project Overview
This project demonstrates a real-world **Data Engineering pipeline** using **PySpark** and **REST APIs**.
Merchant data is ingested from an external API, cleaned, enriched, and stored in Parquet format.

## 🛠 Tech Stack
- Python
- PySpark
- REST API
- Google Colab
- GitHub

## 🏗 Architecture
API → PySpark → Cleaning & Transformation → Parquet Output

## 📥 Data Source
Public REST API:
https://dummyjson.com/users

## 🔄 Data Processing Steps
1. Fetch data from REST API
2. Flatten nested JSON structures
3. Apply explicit schema
4. Clean data (null handling, duplicates)
5. Enhance data (derived columns)
6. Write optimized Parquet output

## ▶ How to Run
```bash
pip install pyspark requests

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MerchantAPIProject") \
    .getOrCreate()

spark
```

---

## 🔹 CELL 2: Fetch Data from REST API

```python
import requests

url = "https://dummyjson.com/users"
response = requests.get(url)

data = response.json()["users"]
len(data)
```

---

## 🔹 CELL 3: Flatten Nested JSON (IMPORTANT)

```python
processed_data = []

for user in data:
    processed_data.append({
        "id": user.get("id"),
        "firstName": user.get("firstName"),
        "lastName": user.get("lastName"),
        "email": user.get("email"),
        "age": user.get("age"),
        "city": user.get("address", {}).get("city"),
        "country": user.get("address", {}).get("country")
    })

processed_data[:2]
```

---

## 🔹 CELL 4: Define Explicit Schema (ERROR FIX)

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("firstName", StringType(), True),
    StructField("lastName", StringType(), True),
    StructField("email", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True),
    StructField("country", StringType(), True)
])
```

---

## 🔹 CELL 5: Create Spark DataFrame

```python
df = spark.createDataFrame(processed_data, schema=schema)
df.printSchema()
df.show(5)
```

---

## 🔹 CELL 6: Data Cleaning

```python
df_clean = (
    df.dropDuplicates()
      .fillna("UNKNOWN")
)

df_clean.count()
```

---

## 🔹 CELL 7: Data Enhancement (Derived Column)

```python
from pyspark.sql.functions import concat_ws, col

df_enhanced = df_clean.withColumn(
    "full_name",
    concat_ws(" ", col("firstName"), col("lastName"))
)

df_enhanced.select("id", "full_name", "email").show(5)
```

---

## 🔹 CELL 8: Business Logic (Filter Adults)

```python
df_final = df_enhanced.filter(col("age") >= 18)
df_final.count()
```

---

## 🔹 CELL 9: Write Output (Parquet)

```python
df_final.write.mode("overwrite").parquet("merchant_output")
```

---

## 🔹 CELL 10: Verify Output

```python
spark.read.parquet("merchant_output").show(5)
```

---

# ✅ THIS PROJECT SHOWS:

✔ PySpark
✔ REST API Integration
✔ Nested JSON handling
✔ Explicit Schema
✔ Data Cleaning & Enrichment
✔ Parquet Output

---

