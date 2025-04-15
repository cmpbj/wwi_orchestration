from sqlalchemy import Column, Integer, String, JSON, Float, DateTime, Date, Boolean, BigInteger
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

class EmployeesData(Base):
    __tablename__ = 'raw_employees'
    __table_args__ = {"schema": "raw"}

    employeeKey = Column(Integer, primary_key=True)
    employee = Column(String, nullable=True)
    preferredName = Column(String, nullable=True)
    isSalesPerson = Column(Boolean, nullable=False)
    photo = Column(String, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class PaymentMethodData(Base):
    __tablename__ = 'raw_payment_method'
    __table_args__ = {"schema": "raw"}

    paymentMethodKey = Column(Integer, primary_key=True)
    paymentMethod = Column(String, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class StockItemData(Base):
    __tablename__ = 'raw_stock_item'
    __table_args__ = {"schema": "raw"}

    stockItemKey = Column(Integer, primary_key=True)
    stockItem = Column(String, nullable=True)
    color = Column(String, nullable=True)
    sellingPackage = Column(String, nullable=True)
    buyingPackage = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    size = Column(String, nullable=True)
    leadTimeDays = Column(Integer, nullable=False)
    quantityPerOuter = Column(Integer, nullable=False)
    isChillerStock = Column(Boolean, nullable=False)
    barcode = Column(String, nullable=True)
    taxRate = Column(Float, nullable=False)
    unitPrice = Column(Float, nullable=False)
    recommendedRetailPrice = Column(Float, nullable=True)
    typicalWeightPerUnit = Column(Float, nullable=False)
    photo = Column(String, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class TransactionTypeData(Base):
    __tablename__ = 'raw_transaction_type'
    __table_args__ = {"schema": "raw"}

    transactionTypeKey = Column(Integer, primary_key=True)
    transactionType = Column(String, nullable=True)
    validFrom = Column(DateTime, nullable=False)
    validTo = Column(DateTime, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class MovementData(Base):
    __tablename__ = 'raw_movements'
    __table_args__ = {"schema": "raw"}

    movementKey = Column(BigInteger, primary_key=True)
    dateKey = Column(DateTime, nullable=False)
    stockItemKey = Column(Integer, nullable=False)
    stockItem = Column(String, nullable=True)
    customerKey = Column(Integer, nullable=True)
    customer = Column(String, nullable=True)
    supplierKey = Column(Integer, nullable=True)
    supplier = Column(String, nullable=True)
    transactionType = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class OrdersData(Base):
    __tablename__ = 'raw_orders'
    __table_args__ = {"schema": "raw"}

    orderKey = Column(BigInteger, primary_key=True)
    cityKey = Column(Integer, nullable=False)
    address = Column(String, nullable=True)
    customerKey = Column(Integer, nullable=False)
    customer = Column(String, nullable=True)
    stockItemKey = Column(Integer, nullable=False)
    stockItem = Column(String, nullable=True)
    orderDateKey = Column(DateTime, nullable=False)
    pickedDateKey = Column(DateTime, nullable=True)
    salespersonKey = Column(Integer, nullable=False)
    pickerKey = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    package = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    unitPrice = Column(Float, nullable=False)
    taxRate = Column(Float, nullable=False)
    totalExcludingTax = Column(Float, nullable=False)
    taxAmount = Column(Float, nullable=False)
    totalIncludingTax = Column(Float, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class PurchaseData(Base):
    __tablename__ = 'raw_purchase'
    __table_args__ = {"schema": "raw"}

    purchaseKey = Column(BigInteger, primary_key=True)
    dateKey = Column(DateTime, nullable=False)
    supplierKey = Column(Integer, nullable=False)
    stockItemKey = Column(Integer, nullable=False)
    orderedOuters = Column(Integer, nullable=False)
    orderedQuantity = Column(Integer, nullable=False)
    receivedOuters = Column(Integer, nullable=False)
    package = Column(String, nullable=True)
    isOrderFinalized = Column(Boolean, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class SalesData(Base):
    __tablename__ = 'raw_sales'
    __table_args__ = {"schema": "raw"}

    saleKey = Column(BigInteger, primary_key=True)
    cityKey = Column(Integer, nullable=False)
    address = Column(String, nullable=True)
    customerKey = Column(Integer, nullable=False)
    billToCustomerKey = Column(Integer, nullable=False)
    stockItemKey = Column(Integer, nullable=False)
    stockItem = Column(String, nullable=True)
    invoiceDateKey = Column(DateTime, nullable=False)
    deliveryDateKey = Column(DateTime, nullable=True)
    salespersonKey = Column(Integer, nullable=False)
    salesPerson = Column(String, nullable=True)
    description = Column(String, nullable=True)
    package = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    unitPrice = Column(Float, nullable=False)
    taxRate = Column(Float, nullable=False)
    totalExcludingTax = Column(Float, nullable=False)
    taxAmount = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    totalIncludingTax = Column(Float, nullable=False)
    totalDryItems = Column(Integer, nullable=False)
    totalChillerItems = Column(Integer, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class StockHoldingData(Base):
    __tablename__ = 'raw_stock_holding'
    __table_args__ = {"schema": "raw"}

    stockHoldingKey = Column(BigInteger, primary_key=True, autoincrement=True)
    stockItemKey = Column(Integer, nullable=False)
    quantityOnHand = Column(Integer, nullable=False)
    binLocation = Column(String, nullable=True)
    lastStocktakeQuantity = Column(Integer, nullable=False)
    lastCostPrice = Column(Float, nullable=False)
    reorderLevel = Column(Integer, nullable=False)
    targetStockLevel = Column(Integer, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)

class TransactionsData(Base):
    __tablename__ = 'raw_transactions'
    __table_args__ = {"schema": "raw"}

    transactionKey = Column(BigInteger, primary_key=True)
    dateKey = Column(DateTime, nullable=False)
    customerKey = Column(Integer, nullable=True)
    customer = Column(String, nullable=True)
    billToCustomerKey = Column(Integer, nullable=True)
    billToCustomer = Column(String, nullable=True)
    supplierKey = Column(Integer, nullable=True)
    supplier = Column(String, nullable=True)
    transactionTypeKey = Column(Integer, nullable=False)
    paymentMethod = Column(String, nullable=True)
    supplierInvoiceNumber = Column(String, nullable=True)
    totalExcludingTax = Column(Float, nullable=False)
    taxAmount = Column(Float, nullable=False)
    totalIncludingTax = Column(Float, nullable=False)
    outstandingBalance = Column(Float, nullable=False)
    isFinalized = Column(Boolean, nullable=False)
    extraction_date = Column(DateTime(timezone=True), default=func.now(), index=True)