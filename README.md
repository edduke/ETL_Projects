# ETL_Projects
This is a repository for ETL projects



This is the Data Architecture Behind this 
[Screenshot 2025-01-04 at 09 18 19](https://github.com/user-attachments/assets/75b045b6-80d7-465a-acf1-d3b13f495a30)

Based off Google Cloud Solutions 
- Cloud Composer for Orchestration (Airflow under the hood) - Runs with python script
- Cloud Storage to hold the raw data
- Cloud Data Fusion to transform the data and encrypt PII DATA
- Big Query to store the cleaned high quality data
- Looker to Visualize the data for end users
