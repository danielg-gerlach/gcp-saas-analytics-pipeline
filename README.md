# SaaS Analytics Data Pipeline on Google Cloud Platform

This project demonstrates a complete, automated, and scalable ELT (Extract, Load, Transform) data pipeline built on Google Cloud Platform. It ingests raw SaaS product usage data, processes it into a clean analytical data warehouse, and visualizes key business metrics in a Looker Studio dashboard.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white)
![Looker](https://img.shields.io/badge/Looker_Studio-4285F4?style=for-the-badge&logo=looker&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

---
## Key Features
* **Automated Ingestion:** A serverless Cloud Function automatically triggers to ingest new raw data files uploaded to a GCS bucket.
* **Scalable Data Warehousing:** Utilizes Google BigQuery for high-performance data storage and transformation.
* **Data Modeling:** Implements a clear distinction between a raw data staging area and a clean, transformed analytics data mart.
* **Business Intelligence:** Calculates critical SaaS metrics like Monthly Active Users (MAU), Customer Churn Rate, and Feature Adoption.
* **Executive Dashboard:** Presents insights through an interactive dashboard built in Looker Studio.

---
## Architecture
The pipeline follows modern cloud best practices, landing raw data in a storage layer before processing it into the data warehouse.

![Data Pipeline Architecture](https://i.imgur.com/K1j11aK.png)

---
## Tech Stack
* **Cloud Provider:** Google Cloud Platform (GCP)
* **Data Lake / Staging:** Google Cloud Storage (GCS)
* **Data Ingestion:** Cloud Functions (Python)
* **Data Warehouse:** Google BigQuery
* **Transformation:** SQL
* **Visualization:** Looker Studio

---
## ELT Process
1.  **Extract & Load:** Raw CSV files (`users.csv`, `events.csv`, `subscriptions.csv`) are uploaded to a GCS bucket (`saas-data-landing-zone`).
2.  **Automated Trigger:** A GCP Cloud Function, subscribed to the GCS bucket, fires upon file upload. It reads the CSV and loads its content into corresponding tables in a `saas_raw_data` dataset in BigQuery.
3.  **Transform:** A series of SQL scripts are executed within BigQuery to clean, join, and aggregate the raw data. The results are materialized into new, optimized tables in a separate `saas_analytics` dataset. This process creates key data models like:
    * `dim_users`: A dimension table with clean user information.
    * `fact_user_activity`: A fact table tracking daily user engagement.
    * `monthly_metrics`: A summary table with pre-calculated KPIs.

---
## Business Metrics & KPIs
The final analytical models provide crucial insights into product performance and user behavior, including:
* Monthly Active Users (MAU)
* Customer Churn Rate
* New User Growth
* Feature Adoption & Popularity
* User Conversion Rate (Free to Paid)

---
## Dashboard Preview
The Looker Studio dashboard connects directly to the `saas_analytics` tables in BigQuery, providing an interactive and always-up-to-date view of the business metrics.

*(placeholder for a screenshot of your finished Looker Studio dashboard)*

---
## Setup & Deployment
1.  **Prerequisites:** Google Cloud SDK, Terraform (optional, for infrastructure as code).
2.  **Configuration:** Set up environment variables for GCP `PROJECT_ID`, `GCS_BUCKET`, and BigQuery `DATASET`.
3.  **Deployment:**
    * Deploy the Cloud Function using the `gcloud` CLI.
    * Execute the SQL transformation scripts in the BigQuery console or via a scheduled query.
