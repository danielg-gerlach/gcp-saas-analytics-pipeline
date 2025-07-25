import os
import pandas as pd
from google.cloud import bigquery, storage

# Initialize clients
storage_client = storage.Client()
bigquery_client = bigquery.Client()

# --- Configuration ---
PROJECT_ID = os.getenv("GCP_PROJECT", "saas-analytics-project-467007")
BIGQUERY_DATASET_ID = os.getenv("BIGQUERY_DATASET", "saas_raw_data")


def ingest_saas_data(event, context):
    """
    Cloud Function triggered by a new file upload to a GCS bucket.
    Reads a CSV file and loads it into a corresponding BigQuery table.
    """
    # Get the file that triggered the function
    bucket_name = event["bucket"]
    file_name = event["name"]

    print(f"Triggered by file: {file_name} from bucket: {bucket_name}")

    # Ensure the file is a CSV
    if not file_name.lower().endswith(".csv"):
        print(f"File {file_name} is not a CSV. Skipping.")
        return

    # Construct a GCS client URI to the file
    uri = f"gs://{bucket_name}/{file_name}"

    try:
        # Read the CSV file from GCS into a pandas DataFrame
        df = pd.read_csv(uri)
        print(f"Successfully read {len(df)} rows from {file_name}.")
    except Exception as e:
        print(f"Error reading CSV from GCS: {e}")
        return

    # Determine the destination table name from the filename
    table_name = file_name.lower().replace(".csv", "")
    table_id = f"{PROJECT_ID}.{BIGQUERY_DATASET_ID}.{table_name}"

    # Configure the BigQuery load job
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition="WRITE_TRUNCATE",
    )

    print(f"Loading data into BigQuery table: {table_id}")

    try:
        # Start the load job
        load_job = bigquery_client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()
        print(f"Successfully loaded data into {table_id}.")

    except Exception as e:
        print(f"Error loading data into BigQuery: {e}")
        # This helps see detailed errors from BigQuery
        if hasattr(e, 'errors'):
            print(f"Error details: {e.errors}")