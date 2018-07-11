from sqlalchemy import (
    and_, asc, Boolean, Column, DateTime, desc, ForeignKey, Integer, or_,
    select, String, Text,
)
from ..main import db

class User(db.Model):
	__tablename__ = 'users'
	id = Column(Integer,primary_key=True)
	username = Column(String,nullable=False)
	password = Column(String,nullable=False)

	