# Sales Data ETL Pipeline (PostgreSQL + AWS S3)

## 📌 Overview
This project implements a **complete end-to-end ETL (Extract, Transform, Load) pipeline** using Python.  
The pipeline processes raw sales data from CSV files, applies business transformations, loads the processed data into a **PostgreSQL database**, and stores both raw and processed data in **AWS S3**.

This project is designed to simulate **real-world Data Engineering workflows** used for analytics, reporting, and downstream data processing.

---

## 🏗️ Architecture

CSV File  
→ Extract (Python, Pandas)  
→ Transform (Feature Engineering)  
→ Load (PostgreSQL Database)  
→ Store (AWS S3)

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Processing:** Pandas  
- **Database:** PostgreSQL  
- **Cloud Storage:** AWS S3  
- **Libraries:** psycopg2, boto3  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

sales-data-etl/
│
├── data/
│ ├── raw/
│ │ └── sales_data.csv
│ └── processed/
│ └── cleaned_sales_data.csv
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│
├── config/
│ └── config.py
│
├── main.py
├── requirements.txt
└── README.md

---

## 📥 Data Source
- **Type:** CSV File  
- **Records:** 1,000+ sales transactions  
- **Columns Include:**  
  - Product details  
  - Sales region and sales representative  
  - Quantity sold, unit price, unit cost  
  - Customer type, payment method, sales channel  

---

## 🔄 ETL Pipeline Details

### 1️⃣ Extract
- Reads raw sales data from a CSV file
- Loads data into a Pandas DataFrame

### 2️⃣ Transform
- Converts date columns to proper datetime format
- Performs feature engineering:
  - Revenue = Quantity × Unit Price
  - Cost = Quantity × Unit Cost
  - Profit = Revenue − Cost
- Produces analytics-ready data

### 3️⃣ Load (Database)
- Loads transformed data into **PostgreSQL**
- Creates a structured table suitable for analytics and BI tools

### 4️⃣ Load (Cloud Storage)
- Uploads:
  - Raw CSV data to AWS S3
  - Processed CSV data to AWS S3
- Maintains clear folder separation (`raw/` and `processed/`)

---

## 🗄️ PostgreSQL Table Schema

```sql
CREATE TABLE sales_data (
    product_id INT,
    sale_date DATE,
    sales_rep VARCHAR(50),
    region VARCHAR(50),
    sales_amount FLOAT,
    quantity_sold INT,
    product_category VARCHAR(50),
    unit_cost FLOAT,
    unit_price FLOAT,
    customer_type VARCHAR(50),
    discount FLOAT,
    payment_method VARCHAR(50),
    sales_channel VARCHAR(50),
    region_and_sales_rep VARCHAR(100),
    revenue FLOAT,
    cost FLOAT,
    profit FLOAT
);
