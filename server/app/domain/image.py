from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from .. import db


class Image(db.Model):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    upload_time = Column(DateTime, nullable=False)
    update_user_id = Column(Integer, ForeignKey("users.id"))
    update_user = relationship('update_user_id', backref=backref('users'))
