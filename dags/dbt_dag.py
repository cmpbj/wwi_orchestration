from airflow import DAG
from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.hooks.base_hook import BaseHook
from datetime import datetime
import os


container_url = Variable.get("CONTAINER_URL")
docker_url = Variable.get('LOGIN_SERVER')
docker_conn = BaseHook.get_connection("docker_registry_conn")


dbt_env = {
    "PROD_USER_NAME": Variable.get("PROD_USER_NAME"),
    "PROD_PASSWORD": Variable.get("PROD_PASSWORD"),
    "PROD_DB_NAME": Variable.get("PROD_DB_NAME"),
    "PROD_SCHEMA": Variable.get("PROD_SCHEMA"),
    "PROD_HOSTNAME": Variable.get("PROD_HOSTNAME"),
    "DBT_DEFAULT_TARGET": "prod",
}

# Define DAG properties
default_args = {
    "start_date": datetime(2025, 3, 29),
    "schedule_interval": "@daily",
    "catchup": False,
}

@dag(
    dag_id='dbt_prod_build',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@daily",  # Only triggered manually or you can put a cron schedule
    catchup=False,
    tags=["dbt", "prod"],
)
def dbt_transformation_dag():

    dbt_deps = DockerOperator(
        task_id='dbt_deps',
        image=container_url,
        api_version='auto',
        auto_remove='success',
        docker_conn_id="docker_registry_conn",
        docker_url=docker_url,
        command='dbt deps',
        environment=dbt_env,
    )

    dbt_build = DockerOperator(
        task_id='dbt_build',
        image=container_url,
        api_version='auto',
        auto_remove='success',
        docker_conn_id="docker_registry_conn",
        docker_url=docker_url,
        command='dbt build',
        environment=dbt_env,
    )

    dbt_deps >> dbt_build

dag_instance = dbt_transformation_dag()
