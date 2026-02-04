# Sales Data ETL Pipeline 

## 📌 Overview
This project implements a production-style end-to-end ETL (Extract, Transform, Load) pipeline using Python.  
The pipeline processes raw sales data from CSV files, applies business and data-quality transformations, loads the processed data into a PostgreSQL database, and archives both raw and processed datasets in AWS S3.

The project reflects real-world Data Engineering workflows, including logging, validation, and performance-aware database loading used in analytics and reporting systems.

---

## 🏗️ Architecture

CSV File  
↓  
Extract (Python, Pandas)  
↓  
Validate (Data Quality Checks)  
↓  
Transform (Feature Engineering)  
↓  
Load (PostgreSQL – Batch Insert)  
↓  
Store (AWS S3 – Raw & Processed)

---

## 🛠️ Tech Stack

- Programming Language: Python  
- Data Processing: Pandas  
- Database: PostgreSQL  
- Cloud Storage: AWS S3  
- Libraries: psycopg2, boto3  
- Logging: Python logging module  
- Version Control: Git & GitHub  

---

## 📥 Data Source
- Type: CSV File  
- Records: 1,000+ sales transactions  
- Columns include:
  - Product details  
  - Sales region and sales representative  
  - Quantity sold, unit price, unit cost  
  - Customer type, payment method, sales channel  

---

## 🔄 ETL Pipeline Details

### 1. Extract
- Reads raw sales data from a CSV file
- Loads data into a Pandas DataFrame
- Logs extraction status and failures

### 2. Validate
- Checks for null values in critical columns
- Ensures no negative values in quantity or pricing fields
- Verifies valid date formats  
- Prevents bad data from entering downstream systems

### 3. Transform
- Converts date columns to proper datetime format
- Performs feature engineering:
  - Revenue = Quantity × Unit Price
  - Cost = Quantity × Unit Cost
  - Profit = Revenue − Cost
- Produces analytics-ready data

### 4. Load (PostgreSQL)
- Loads transformed data into PostgreSQL
- Uses batch inserts for improved performance
- Creates structured tables suitable for analytics and BI tools

### 5. Load (AWS S3)
- Uploads raw CSV data to AWS S3
- Uploads processed CSV data to AWS S3
- Maintains clear separation between raw and processed datasets

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
