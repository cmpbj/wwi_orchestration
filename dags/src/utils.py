import requests
import json
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from dags.src.database import engine, Base, get_db
from dags.src.models import (
    HolidaysData,
    CitiesData,
    CustomersData,
    EmployeesData,
    PaymentMethodData,
    StockItemData,
    TransactionTypeData,
    MovementData,
    OrdersData,
    PurchaseData,
    SalesData,
    StockHoldingData,
    TransactionsData,
)


HOLIDAY_URL_BASE = "https://brasilapi.com.br/api/feriados/v1/"
WORLD_IMPORTERS_URL = "https://demodata.grapecity.com/wwi/api/v1/"
DB = next(get_db())

def extract_holiday(date, url=HOLIDAY_URL_BASE):
    response = requests.get(f"{url}{date}")
    response = response.json()
    return response

def extract_world_importers(endpoint, url=WORLD_IMPORTERS_URL):
    response = requests.get(f"{url}{endpoint}")
    response = response.json()
    return response

def holiday_func(date, db=DB):
    schema_name = "raw"
    db.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
    db.commit()

    HolidaysData.__table__.create(bind=engine, checkfirst=True)
    data = extract_holiday(date)
    try:
        for record in data:
            holiday = HolidaysData(
                date=record.get("date"),
                name=record.get("name"),
                type=record.get("type"),
            )
            db.add(holiday)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error loading data: {e}")

def load_data(model_class=None, endpoint=None, db=DB):
    if model_class is None:
        raise ValueError("Model class must be provided")

    schema_name = "raw"
    db.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
    db.commit()

    table_name = model_class.__tablename__
    schema_name = "raw"
    db.execute(text(f'DROP TABLE IF EXISTS {schema_name}.{table_name} CASCADE'))
    db.commit()
    model_class.__table__.create(bind=db.get_bind())

    data = extract_world_importers(endpoint)

    try:
        for record in data:
            entry = model_class(**record)
            db.add(entry)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error loading data into {model_class.__tablename__}: {e}")


def employees_func(endpoint):
    load_data(model_class=EmployeesData, endpoint=endpoint)

def payment_method_func(endpoint):
    load_data(model_class=PaymentMethodData, endpoint=endpoint)

def stock_item_func(endpoint):
    load_data(model_class=StockItemData, endpoint=endpoint)

def transaction_type_func(endpoint):
    load_data(model_class=TransactionTypeData, endpoint=endpoint)

def movement_func(endpoint):
    load_data(model_class=MovementData, endpoint=endpoint)

def orders_func(endpoint):
    load_data(model_class=OrdersData, endpoint=endpoint)

def purchase_func(endpoint):
    load_data(model_class=PurchaseData, endpoint=endpoint)

def sales_func(endpoint):
    load_data(model_class=SalesData, endpoint=endpoint)

def stock_holding_func(endpoint):
    load_data(model_class=StockHoldingData, endpoint=endpoint)

def transactions_func(endpoint):
    load_data(model_class=TransactionsData, endpoint=endpoint)

def cities_func(endpoint):
    load_data(model_class=CitiesData, endpoint=endpoint)

def customers_func(endpoint):
    load_data(model_class=CustomersData, endpoint=endpoint)
