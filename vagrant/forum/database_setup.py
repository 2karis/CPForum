import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///lesshome.db')

Base.metadata.create_all(engine)

class Homeless(Base):
	__tablename__ = 'homeless'

	id = Column(Integer, primary_key=True)
	location = Column(String(255), unique = True)
	description = Column(String(255))
	image = Column(String(80))