Airflow ETL Pipeline for Random User Data

This repository contains an Apache Airflow ETL (Extract, Transform, Load) pipeline for fetching random user data from the "Random User Generator" API, transforming it, and loading it into a PostgreSQL database.
Table of Contents

    Prerequisites
    Installation
    Usage
    DAG Overview
    Customization
    Contributing
    License

Prerequisites

Before running this ETL pipeline, ensure you have the following prerequisites installed and configured:

    Apache Airflow: You should have Apache Airflow installed on your system or a running Airflow instance.

    PostgreSQL Database: You need access to a PostgreSQL database where the transformed data will be loaded.

    Python Dependencies: Install the required Python libraries listed in the requirements.txt file.

Installation

    Clone this repository to your local machine:

    bash

git clone https://github.com/yourusername/random-user-etl.git
cd random-user-etl

Install the Python dependencies:

bash

    pip install -r requirements.txt

    Configure your Airflow environment and set up the PostgreSQL database connection in Airflow. You can do this by editing the Airflow configuration files.

    Place the random_user.py DAG file in your Airflow DAGs folder.

Usage

    Start the Airflow scheduler and web interface. Ensure that your DAG is successfully detected.

    Access the Airflow web interface (usually at http://localhost:8080).

    Trigger the random_user_etl DAG manually or let it run according to the defined schedule.

    Monitor the progress and logs of each task in the Airflow UI.

DAG Overview

The Airflow DAG (random_user_etl) consists of the following tasks:

    extract_data: This task extracts random user data from the "Random User Generator" API using a Python callable.

    transform_data: The extracted data is transformed into a structured format by cleaning and restructuring it.

    load_data_to_postgres: The cleaned data is loaded into a PostgreSQL database table.

The DAG is scheduled to run daily At Midnight, but you can customize the schedule interval as needed.

Customization

You can customize this ETL pipeline to fit your specific requirements:

    Adjust the API URL in the random_user.py DAG file if you want to fetch data from a different source or modify the API parameters.

    Modify the transformation logic in the transform_data function to meet your data processing needs.

    Update the PostgreSQL database connection details in the random_user.py DAG file to connect to your database.

    Customize the schedule interval based on your data update frequency.

Contributing

If you'd like to contribute to this project, please follow the standard GitHub fork and pull request workflow. Feel free to open issues for bug reports, feature requests, or other feedback.
License

This project is licensed under the MIT License. See the LICENSE file for details.
