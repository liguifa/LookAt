from sqlalchemy import Column, Integer, String, ForeignKey  # NOQA
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from ..main import db


class Menu(db.Model):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    display_name = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
    parent_id = Column(ForeignKey('menus.id'))
    url = Column(String, nullable=False)
    # parent = relationship('menus', backref=backref('addr'))
