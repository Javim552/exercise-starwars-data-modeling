import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
     __tablename__= "user"
     id = Column(Integer, primary_key=True)
     nameUser = Column(String(250), nullable=False)
     lastNameUser= Column(String(250), nullable=False)
     suscriptionDate = Column(Integer)
     # favPlanets = relationship("Favplanets")
     # favCharacer = relationship("Favcharacters")
     idfavoritos = Column(Integer, ForeignKey("favoritos.id"))
     favoritos = relationship("Favoritos")



                        
class Planets(Base):
     __tablename__ = 'planets'                   
     id = Column(Integer, primary_key=True)
     namePlanet = Column(String(250), nullable=False)
     poblation = Column(Integer)

class Character(Base):
     __tablename__ = 'characters'
     id = Column(Integer, primary_key=True)
     namePerson = Column(String(250))
     secondNamePerson = Column(String(250))




class Favoritos(Base):
     __tablename__= "favoritos"
     id = Column(Integer, primary_key=True)
     idPlanet = Column(Integer, ForeignKey("planets.id"))
     
     idCharacter = Column(Integer, ForeignKey("characters.id"))
    
  


     





def to_dict(self):
     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
