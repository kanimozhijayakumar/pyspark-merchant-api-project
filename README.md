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
