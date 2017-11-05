from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Homeless, Base

engine = create_engine('sqlite:///lesshome.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

location1 = Homeless(location="Peachtree Street", description="One is sick", image="16029849_BG1.jpg")

session.add(location1)
session.commit()

location2 = Homeless(location="Peachtree Blvd", description="He's lonely", image="16029849_BG1.jpg")

session.add(location2)
session.commit()

location3 = Homeless(location="Peachtree Rd", description="This one is hungry", image="16029849_BG1.jpg")

session.add(location3)
session.commit()

location4 = Homeless(location="Peachtree Dr", description="She is cold", image="DSC_0100.jpg")

session.add(location4)
session.commit()

location5 = Homeless(location="Bell Street", description="She twerking, lol", image="Homeless-Encampment-on-Coca-Cola-Place-in-Atlanta-GA-2016-01-16-16.27.13-Kimberly-Krautter-e1486168985572.jpg")

session.add(location5)
session.commit()

location6 = Homeless(location="Memorial Dr", description="He's a teenanger", image="Peachtree Pine.jpg")

session.add(location6)
session.commit()

location7 = Homeless(location="Oak Street", description="Look at the couch", image="Teen underpass.jpg")

session.add(location7)
session.commit()

location8 = Homeless(location="East Atlanta Ave", description="Preach", image="Under i-85 .jpg")

session.add(location8)
session.commit()

location9 = Homeless(location="Marrietta Street", description="Salute", image="homeless church.jpg")

session.add(location9)
session.commit()

location10 = Homeless(location="Hill Street", description="Look at his clean sneakers", image="i-85 collapse.jpg")

session.add(location10)
session.commit()

location11 = Homeless(location="North Ave", description="Chik-fil-a cares", image="i-85 displacement.jpg")

session.add(location11)
session.commit()

location12 = Homeless(location="Ponce De Leon", description="What a nice guy", image="tent-village-4.jpg")

session.add(location12)
session.commit()