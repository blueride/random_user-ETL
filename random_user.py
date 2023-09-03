from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
import pandas as pd
import requests
from sqlalchemy import create_engine

# Declaration of Variables
url = 'https://randomuser.me/api/?results=100'
engine = create_engine('postgresql://Clement:Clem2009@host.docker.internal:5432/random_user_generator')

def get_json_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def transform_data(data):
    # Transform the data as per assignment requirements
    cleaned_data = []
    for user in data['results']:
        # Extract the "number" and "name" fields from the street address dictionary
        street_number = str(user['location']['street']['number'])
        street_name = user['location']['street']['name']
        
        # Concatenate the "number" and "name" to form the street address
        street_address = f"{street_number} {street_name}"
        
        user_info = {
            'First Name': user['name']['first'],
            'Last Name': user['name']['last'],
            'Gender': user['gender'],
            'Email': user['email'],
            'Date of Birth': user['dob']['date'][:10],  # Extract YYYY-MM-DD
            'Country': user['location']['country'],
            'Street Address': street_address,
            'City': user['location']['city'],
            'State': user['location']['state'],
            'Postcode': user['location']['postcode'],
            'Phone': user['phone'],
            'Cell': user['cell']
        }
        cleaned_data.append(user_info)
    
    return cleaned_data


def load_data_to_postgres(data, table_name, connection):
    df = pd.DataFrame(data)
    df.to_sql(table_name, con=connection, if_exists='replace', index=False)


default_args = {
    'owner': 'Abuga',
    'retries': 2,
    'start_date': datetime(2023, 9, 2),
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='random_user_etl',
    description='ETL pipeline for random user data',
    schedule_interval= "0 0 * * *",  # Daily at midnight
    default_args=default_args
) as dag:
    # Task 1: Extract data from the API
    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=get_json_data,
        op_args=[url]
    )

    # Task 2: Transform the data
    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_args=[task_extract.output],
    )

    # Task 3: Load data into PostgreSQL
    task_load = PythonOperator(
        task_id='load_data_to_postgres',
        python_callable=load_data_to_postgres,
        op_args=[task_transform.output, 'random_user_data', engine],
    )

    # Set task dependencies
    task_extract >> task_transform >> task_load