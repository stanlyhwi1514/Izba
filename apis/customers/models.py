import datetime
from extensions import db
from sqlalchemy import Column, DateTime, String, func,ForeignKey,Text
from sqlalchemy.orm import relationship
from base.models import BaseModel


class User(BaseModel, db.Model):
    __tablename__ = 'customers'
    
    name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False)
    designation = Column(String(50), nullable=True)
