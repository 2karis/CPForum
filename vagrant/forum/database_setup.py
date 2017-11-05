from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Homeless(Base):
	__tablename__ = 'homeless'

	id = Column(Integer, primary_key=True)
	location = Column(String(255), unique = True)
	description = Column(String(255))
	image = Column(String(80))

	# @property
	# def serialize(self):
	# 	#Returns object in easily serializaeble format
	# 	return {
	# 	'id': self.id,
	# 	'location': self.location,
	# 	'image': self.image,
	# 	}

	def __repr__(self):
		return "<Homeless(location='%s', description='%s', image='%s')>" % (
        	self.location, self.description, self.image)

engine = create_engine('sqlite:///lesshome.db')

Base.metadata.create_all(engine)