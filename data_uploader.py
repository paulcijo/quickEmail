import csv
import json
import os
import mysql.connector
from celery_main import app

@app.task
def read_and_upload_csv(list_id, csv_file_path):
    try:
        # Establish a database connection
        db_config = {
            'user': os.getenv("MYSQL_USERNAME"),
            'password': os.getenv("MYSQL_PASSWORD"),
            'database': os.getenv("MYSQL_DATABASE"),
            'host': os.getenv("MYSQL_HOST"),
            'port': os.getenv("MYSQL_PORT"),
        }
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Open and read the CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            batch_size = 100  # Adjust batch size as needed

            rows = []
            for row in csv_reader:
                # Convert the row into JSON data
                data = json.dumps(row)
                rows.append((data, list_id))

                if len(rows) >= batch_size:
                    # Batch insert
                    insert_query = (
                        "INSERT INTO uploaded_data (data, list_id) "
                        "VALUES (%s, %s)"
                    )
                    cursor.executemany(insert_query, rows)
                    conn.commit()
                    rows = []

            # Insert any remaining rows
            if rows:
                insert_query = (
                    "INSERT INTO uploaded_data (data, list_id) "
                    "VALUES (%s, %s)"
                )
                cursor.executemany(insert_query, rows)
                conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()
        print(f"CSV data uploaded successfully to list_id: {self.list_id}")
    except Exception as e:
        print(f"Error uploading CSV data: {str(e)}")

