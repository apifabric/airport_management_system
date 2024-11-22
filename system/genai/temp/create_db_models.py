# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Airport(Base):
    """
    description: Represents an airport entity with its location details
    """

    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)



class Airplane(Base):
    """
    description: Represents an airplane with its capacity and airport of residence
    """

    __tablename__ = 'airplane'

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    
    passenger_count = Column(Integer, default=0, nullable=False)  # for count rule



class Passenger(Base):
    """
    description: Represents a passenger with boarding flight and seat details
    """

    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    seat_number = Column(String, nullable=False)



class Flight(Base):
    """
    description: Represents a flight connecting two airports with a scheduled time
    """

    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    airplane_id = Column(Integer, ForeignKey('airplane.id'), nullable=False)
    departure_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)



# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Create test data for Airport
airport1 = Airport(name="JFK International", code="JFK", city="New York", country="USA")
airport2 = Airport(name="Los Angeles International", code="LAX", city="Los Angeles", country="USA")
airport3 = Airport(name="London Heathrow", code="LHR", city="London", country="UK")
airport4 = Airport(name="Tokyo Narita", code="NRT", city="Tokyo", country="Japan")

# Create test data for Airplane
airplane1 = Airplane(model="Boeing 737", seating_capacity=180, airport_id=1, passenger_count=2)
airplane2 = Airplane(model="Airbus A380", seating_capacity=500, airport_id=2, passenger_count=3)
airplane3 = Airplane(model="Embraer 175", seating_capacity=80, airport_id=1, passenger_count=1)
airplane4 = Airplane(model="CRJ 900", seating_capacity=90, airport_id=3, passenger_count=0)

# Create test data for Flight
flight1 = Flight(flight_number="A101", airplane_id=1, departure_airport_id=1, arrival_airport_id=2, departure_time=date(2023, 11, 28), arrival_time=date(2023, 11, 28))
flight2 = Flight(flight_number="B202", airplane_id=2, departure_airport_id=3, arrival_airport_id=4, departure_time=date(2023, 11, 29), arrival_time=date(2023, 11, 29))
flight3 = Flight(flight_number="C303", airplane_id=3, departure_airport_id=2, arrival_airport_id=1, departure_time=date(2023, 11, 30), arrival_time=date(2023, 11, 30))
flight4 = Flight(flight_number="D404", airplane_id=4, departure_airport_id=4, arrival_airport_id=3, departure_time=date(2023, 12, 1), arrival_time=date(2023, 12, 1))

# Create test data for Passenger
passenger1 = Passenger(name="John Doe", flight_id=1, seat_number="12A")
passenger2 = Passenger(name="Jane Smith", flight_id=1, seat_number="14B")
passenger3 = Passenger(name="Ahmed Khan", flight_id=2, seat_number="1A")
passenger4 = Passenger(name="Li Wei", flight_id=2, seat_number="5C")


session.add_all([airport1, airport2, airport3, airport4, airplane1, airplane2, airplane3, airplane4, flight1, flight2, flight3, flight4, passenger1, passenger2, passenger3, passenger4])
session.commit()
