from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, Date
from sqlalchemy.sql import func
from dags.src.database import Base

class HolidaysData(Base):
    __tablename__ = "brazil_holidays"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class CitiesData(Base):
    __tablename__ = "raw_cities"
    __table_args__ = {"schema": "raw"}

    cityKey = Column(Integer, primary_key=True)
    city = Column(String, nullable=True)
    stateProvince = Column(String, nullable=True)
    country = Column(String, nullable=True)
    continent = Column(String, nullable=True)
    salesTerritory = Column(String, nullable=True)
    region = Column(String, nullable=True)
    subregion = Column(String, nullable=True)
    latestRecordedPopulation = Column(Integer, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class CustomersData(Base):
    __tablename__ = "raw_customers"
    __table_args__ = {"schema": "raw"}

    customerKey = Column(Integer, primary_key=True)
    customer = Column(String, nullable=True)
    billToCustomer = Column(String, nullable=True)
    category = Column(String, nullable=True)
    buyingGroup = Column(String, nullable=True)
    primaryContact = Column(String, nullable=True)
    postalCode = Column(String, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)