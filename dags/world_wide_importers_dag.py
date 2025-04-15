from airflow import DAG
from airflow.decorators import task, dag
from airflow.models import Variable
from datetime import datetime
from dags.src.utils import (
    cities_func,
    customers_func,
    employees_func,
    payment_method_func,
    stock_item_func,
    transaction_type_func,
    movement_func,
    orders_func,
    purchase_func,
    sales_func,
    stock_holding_func,
    transactions_func,
)

# Define DAG properties
default_args = {
    "start_date": datetime(2025, 3, 29),
    "schedule_interval": "@daily",
    "catchup": False,
}

@dag(default_args=default_args, schedule_interval="@daily", catchup=False)
def wwi_ingestion_dag():
    @task
    def cities_ingestion():
        cities_func(endpoint="cities")

    @task
    def customers_ingestion():
        customers_func(endpoint="customers")

    @task
    def employees_ingestion():
        employees_func(endpoint="employees")

    @task
    def payment_method_ingestion():
        payment_method_func(endpoint="paymentMethods")

    @task
    def stock_item_ingestion():
        stock_item_func(endpoint="stockItems")

    @task
    def transaction_type_ingestion():
        transaction_type_func(endpoint="transactionTypes")

    @task
    def movement_ingestion():
        movement_func(endpoint="movements")

    @task
    def orders_ingestion():
        orders_func(endpoint="orders")

    @task
    def purchase_ingestion():
        purchase_func(endpoint="purchases")

    @task
    def sales_ingestion():
        sales_func(endpoint="sales")

    @task
    def stock_holding_ingestion():
        stock_holding_func(endpoint="stockHoldings")

    @task
    def transactions_ingestion():
        transactions_func(endpoint="transactions")

    # Execute all tasks independently
    cities_ingestion()
    customers_ingestion()
    employees_ingestion()
    payment_method_ingestion()
    stock_item_ingestion()
    transaction_type_ingestion()
    movement_ingestion()
    orders_ingestion()
    purchase_ingestion()
    sales_ingestion()
    stock_holding_ingestion()
    transactions_ingestion()

# Instantiate the DAG
dag_instance = wwi_ingestion_dag()