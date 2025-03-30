import requests
import json
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from dags.src.models import HolidaysData, CitiesData, CustomersData
from dags.src.database import engine, Base, get_db

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

    Base.metadata.create_all(bind=engine)
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

def cities_func(endpoint, db=DB):
    schema_name = "raw"
    db.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
    db.commit()

    CitiesData.__table__.drop(bind=engine, checkfirst=True)
    CitiesData.__table__.create(bind=engine)

    # Extract data from the source
    data = extract_world_importers(endpoint)

    # Insert new data
    try:
        for record in data:
            city = CitiesData(
                cityKey=record.get("cityKey"),
                city=record.get("city"),
                stateProvince=record.get("stateProvince"),
                country=record.get("country"),
                continent=record.get("continent"),
                salesTerritory=record.get("salesTerritory"),
                region=record.get("region"),
                subregion=record.get("subregion"),
                latestRecordedPopulation=record.get("latestRecordedPopulation"),
                validFrom=record.get("validFrom"),
                validTo=record.get("validTo"),
            )
            db.add(city)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error loading data: {e}")

def customers_func(endpoint, db=DB):
    schema_name = "raw"
    db.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
    db.commit()

    CustomersData.__table__.drop(bind=engine, checkfirst=True)
    CustomersData.__table__.create(bind=engine)

    # Extract data from the source
    data = extract_world_importers(endpoint)

    # Insert new data
    try:
        for record in data:
            customer = CustomersData(
                customerKey=record.get("customerKey"),
                customer=record.get("customer"),
                billToCustomer=record.get("billToCustomer"),
                category=record.get("category"),
                buyingGroup=record.get("buyingGroup"),
                primaryContact=record.get("primaryContact"),
                postalCode=record.get("postalCode"),
                validFrom=record.get("validFrom"),
                validTo=record.get("validTo"),
            )
            db.add(customer)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error loading data: {e}")