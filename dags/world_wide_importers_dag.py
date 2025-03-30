from airflow import DAG
from airflow.decorators import task, dag
from airflow.models import Variable
from datetime import datetime
from dags.src.utils import cities_func, customers_func

# Define DAG properties
default_args = {
    "start_date": datetime(2025, 3, 29),
    "schedule": "@daily",
    "catchup": False,
}

@dag(**default_args)
def wwi_ingestion_dag():
    @task
    def cities_ingestion():
        cities_func(endpoint="cities")

    @task
    def customers_ingestion():
        customers_func(endpoint="customers")

    [cities_ingestion(), customers_ingestion()]

dag_instance = wwi_ingestion_dag()
