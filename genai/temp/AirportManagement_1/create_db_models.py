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
    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    location = Column(String(100))

    """description: Table for storing airport details such as name and location."""


class Airplane(Base):
    __tablename__ = 'airplane'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String(100))
    seating_capacity = Column(Integer)
    airport_id = Column(Integer, ForeignKey('airport.id'))

    """description: Table for storing airplane details, including model and seating capacity, associated with an airport."""


class Flight(Base):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String(10))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    airplane_id = Column(Integer, ForeignKey('airplane.id'))

    """description: Table for storing flight details, including flight number, departure, and arrival times, associated with an airplane."""


class Passenger(Base):
    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))

    """description: Table for storing passenger personal details such as name and email."""


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'))
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    seat_number = Column(String(5))

    """description: Table for storing booking information, linking passengers to flights and including seat assignments."""


class Baggage(Base):
    __tablename__ = 'baggage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    weight = Column(Integer)
    booking_id = Column(Integer, ForeignKey('booking.id'))

    """description: Table for storing baggage details such as weight, associated with a booking."""


class CrewMember(Base):
    __tablename__ = 'crew_member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(String(50))
    flight_id = Column(Integer, ForeignKey('flight.id'))

    """description: Table for storing crew member details, including name, role, and associated flight."""


class Maintenance(Base):
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    airplane_id = Column(Integer, ForeignKey('airplane.id'))
    date = Column(DateTime)
    description = Column(String(200))

    """description: Table for storing maintenance records for airplanes, including date and description of maintenance work."""


class FoodService(Base):
    __tablename__ = 'food_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'))
    meal_type = Column(String(50))
    description = Column(String(200))

    """description: Table for storing food service details provided on flights, including type and description."""


class TicketAgent(Base):
    __tablename__ = 'ticket_agent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    agency_name = Column(String(100))

    """description: Table for storing ticket agent details including name and associated agency."""


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))
    ticket_agent_id = Column(Integer, ForeignKey('ticket_agent.id'))

    """description: Table for storing reservation details, linking passengers, flights, and ticket agents."""


class AirplaneType(Base):
    __tablename__ = 'airplane_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(100))
    manufacturer = Column(String(100))

    """description: Table for storing airplane type details including model name and manufacturer."""


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

test_data = """
from datetime import datetime, date

airport1 = Airport(name='John F. Kennedy International', location='New York, NY')
airport2 = Airport(name='Los Angeles International', location='Los Angeles, CA')
airport3 = Airport(name='Heathrow', location='London, UK')
airport4 = Airport(name='Haneda', location='Tokyo, JP')

airplane1 = Airplane(model='Boeing 737', seating_capacity=180, airport_id=1)
airplane2 = Airplane(model='Airbus A320', seating_capacity=150, airport_id=2)
airplane3 = Airplane(model='Boeing 777', seating_capacity=300, airport_id=3)
airplane4 = Airplane(model='Airbus A380', seating_capacity=500, airport_id=4)

flight1 = Flight(flight_number='AA100', departure_time=datetime(2023, 1, 15, 6, 0), arrival_time=datetime(2023, 1, 15, 12, 0), airplane_id=1)
flight2 = Flight(flight_number='BA200', departure_time=datetime(2023, 1, 15, 14, 0), arrival_time=datetime(2023, 1, 15, 20, 0), airplane_id=2)
flight3 = Flight(flight_number='DL300', departure_time=datetime(2023, 1, 16, 8, 0), arrival_time=datetime(2023, 1, 16, 14, 0), airplane_id=3)
flight4 = Flight(flight_number='UA400', departure_time=datetime(2023, 1, 17, 10, 0), arrival_time=datetime(2023, 1, 17, 16, 0), airplane_id=4)

passenger1 = Passenger(first_name='John', last_name='Doe', email='john.doe@example.com')
passenger2 = Passenger(first_name='Jane', last_name='Smith', email='jane.smith@example.com')
passenger3 = Passenger(first_name='Alice', last_name='Johnson', email='alice.johnson@example.com')
passenger4 = Passenger(first_name='Bob', last_name='Brown', email='bob.brown@example.com')

booking1 = Booking(flight_id=1, passenger_id=1, seat_number='12A')
booking2 = Booking(flight_id=2, passenger_id=2, seat_number='7B')
booking3 = Booking(flight_id=3, passenger_id=3, seat_number='14C')
booking4 = Booking(flight_id=4, passenger_id=4, seat_number='1D')

baggage1 = Baggage(weight=20, booking_id=1)
baggage2 = Baggage(weight=25, booking_id=2)
baggage3 = Baggage(weight=18, booking_id=3)
baggage4 = Baggage(weight=22, booking_id=4)

crew_member1 = CrewMember(first_name='Mike', last_name='Clark', role='Pilot', flight_id=1)
crew_member2 = CrewMember(first_name='Sophie', last_name='Turner', role='Co-Pilot', flight_id=2)
crew_member3 = CrewMember(first_name='Kate', last_name='Williams', role='Flight Attendant', flight_id=3)
crew_member4 = CrewMember(first_name='James', last_name='Taylor', role='Engineer', flight_id=4)

maintenance1 = Maintenance(airplane_id=1, date=datetime(2023, 1, 10, 9, 0), description='Engine Check')
maintenance2 = Maintenance(airplane_id=2, date=datetime(2023, 1, 11, 10, 0), description='Wheel Inspection')
maintenance3 = Maintenance(airplane_id=3, date=datetime(2023, 1, 12, 11, 0), description='Fuselage Repair')
maintenance4 = Maintenance(airplane_id=4, date=datetime(2023, 1, 13, 12, 0), description='Avionics Update')

food_service1 = FoodService(flight_id=1, meal_type='Breakfast', description='Continental Breakfast')
food_service2 = FoodService(flight_id=2, meal_type='Lunch', description='Chicken and Vegetables')
food_service3 = FoodService(flight_id=3, meal_type='Dinner', description='Beef and Potatoes')
food_service4 = FoodService(flight_id=4, meal_type='Snack', description='Fruit and Cheese Plate')

ticket_agent1 = TicketAgent(first_name='Paul', last_name='Walker', agency_name='Travel Experts')
ticket_agent2 = TicketAgent(first_name='Emma', last_name='Stone', agency_name='Flight Network')
ticket_agent3 = TicketAgent(first_name='Robert', last_name='Downey Jr.', agency_name='Sky Miles')
ticket_agent4 = TicketAgent(first_name='Jennifer', last_name='Lawrence', agency_name='Air Pioneers')

reservation1 = Reservation(passenger_id=1, flight_id=1, ticket_agent_id=1)
reservation2 = Reservation(passenger_id=2, flight_id=2, ticket_agent_id=2)
reservation3 = Reservation(passenger_id=3, flight_id=3, ticket_agent_id=3)
reservation4 = Reservation(passenger_id=4, flight_id=4, ticket_agent_id=4)

airplane_type1 = AirplaneType(model_name='737-900', manufacturer='Boeing')
airplane_type2 = AirplaneType(model_name='A321', manufacturer='Airbus')
airplane_type3 = AirplaneType(model_name='787 Dreamliner', manufacturer='Boeing')
airplane_type4 = AirplaneType(model_name='A380', manufacturer='Airbus')
"""


session.add_all([airport1, airport2, airport3, airport4, airplane1, airplane2, airplane3, airplane4, flight1, flight2, flight3, flight4, passenger1, passenger2, passenger3, passenger4, booking1, booking2, booking3, booking4, baggage1, baggage2, baggage3, baggage4, crew_member1, crew_member2, crew_member3, crew_member4, maintenance1, maintenance2, maintenance3, maintenance4, food_service1, food_service2, food_service3, food_service4, ticket_agent1, ticket_agent2, ticket_agent3, ticket_agent4, reservation1, reservation2, reservation3, reservation4, airplane_type1, airplane_type2, airplane_type3, airplane_type4])
session.commit()
