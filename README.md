# Olist E-Commerce Data Pipeline & Analytics Dashboard

An end-to-end data engineering and analytics project analyzing nearly 100,000 orders from the Olist Brazilian e-commerce dataset. This project demonstrates a complete ETL (Extract, Transform, Load) pipeline, culminating in an interactive web dashboard for business intelligence.

## Dashboard Preview
![Dashboard Preview](dashboard-sc-1.png)
![Dashboard Preview](dashboard-sc-2.png)

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Database:** SQLite
* **Frontend/Visualization:** Streamlit
* **Version Control:** Git & GitHub

## Architecture & ETL Workflow
1. **Extract:** Ingested relational raw data (Orders and Customers) from static CSV files.
2. **Transform:** Performed memory-optimized inner joins using Pandas to map specific customer demographics to their individual order lifecycles.
3. **Load:** Persisted the denormalized data into a local SQLite database (`ecommerce_data.db`) for robust, query-ready storage.
4. **Deploy:** Built a Streamlit web application that queries the SQLite database in real-time to generate KPIs and dynamic categorical visualizations.

## How to Run Locally
*Note: For security and repository optimization, raw datasets and the SQLite database are intentionally excluded from version control. You must run the ingestion script to generate the database.*

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Shash09090/olist-ecom-analytics](https://github.com/Shash09090/olist-ecom-analytics)
   cd olist_ecom_analytics