# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 22, 2024 15:58:54
# Database: sqlite:////tmp/tmp.aiP0yZ8gnf-01JDA9EXBS55PGB7NR4EGT1695/AirportManagement/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Airport(SAFRSBaseX, Base):
    """
    description: Represents an airport entity with its location details
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    AirplaneList : Mapped[List["Airplane"]] = relationship(back_populates="airport")
    FlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.arrival_airport_id]', back_populates="arrival_airport")
    departureFlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.departure_airport_id]', back_populates="departure_airport")



class Airplane(SAFRSBaseX, Base):
    """
    description: Represents an airplane with its capacity and airport of residence
    """
    __tablename__ = 'airplane'
    _s_collection_name = 'Airplane'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)
    airport_id = Column(ForeignKey('airport.id'), nullable=False)
    passenger_count = Column(Integer, nullable=False)

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("AirplaneList"))

    # child relationships (access children)
    FlightList : Mapped[List["Flight"]] = relationship(back_populates="airplane")



class Flight(SAFRSBaseX, Base):
    """
    description: Represents a flight connecting two airports with a scheduled time
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    airplane_id = Column(ForeignKey('airplane.id'), nullable=False)
    departure_airport_id = Column(ForeignKey('airport.id'), nullable=False)
    arrival_airport_id = Column(ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    airplane : Mapped["Airplane"] = relationship(back_populates=("FlightList"))
    arrival_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.arrival_airport_id]', back_populates=("FlightList"))
    departure_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.departure_airport_id]', back_populates=("departureFlightList"))

    # child relationships (access children)
    PassengerList : Mapped[List["Passenger"]] = relationship(back_populates="flight")



class Passenger(SAFRSBaseX, Base):
    """
    description: Represents a passenger with boarding flight and seat details
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    seat_number = Column(String, nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("PassengerList"))

    # child relationships (access children)
