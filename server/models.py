from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String) # Plain text for week 1 demo only

class Device(Base):
    __tablename__ = "devices"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parents.id"))

class Heartbeat(Base):
    __tablename__ = "heartbeats"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, ForeignKey("devices.id"))
    timestamp = Column(DateTime, default=func.now())
    status = Column(String)
    policy_version = Column(Integer)
