from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, Table, ForeignKey, Integer
from typing import List

db = SQLAlchemy()

# Usuarios
# personajes
# planetas
# favoritos

# relaciones

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite: Mapped["Favorite"] = relationship(back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[str] = mapped_column(nullable=False)
    homeworld : Mapped[int] = mapped_column(ForeignKey("planet.id"))

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "gender" : self.gender,
            "hair_color" : self.hair_color,
            "eye_color" : self.eye_color,
            "height" : self.height
            
        }
    
class Planet(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate : Mapped[str] = mapped_column(nullable=False)
    population : Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "climate" : self.climate,
            "population" : self.population
        }
    
class Vehicle(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    cost_in_credits : Mapped[str] = mapped_column(nullable=False)
    manufacturer : Mapped[str] = mapped_column(nullable=False)
    vehicle_class : Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "cost_in_credits" : self.cost_in_credits,
            "manufacturer" : self.manufacturer,
            "vehicle_class" : self.vehicle_class
        }

class Favorite(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    user : Mapped[int] = mapped_column(ForeignKey("user.id"))
    planet : Mapped[int] = mapped_column(ForeignKey("planet.id"))


    user : Mapped["User"] = relationship(back_populates="favorite")


    def serialize(self):
        return {
            "id" : self.id,
            "user_id" : self.user
        }