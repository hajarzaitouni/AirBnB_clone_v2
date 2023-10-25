#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay

    Attributes:
        __tablename__ (Str): MySQL's table name to store places.
        city_id (String): place's city id.
        user_id (String): place's user id.
        name (String): place's name.
        description (String): place's description.
        number_rooms (Integer): number of rooms.
        number_bathrooms (Integer): number of bathrooms.
        max_guest (Integer): maximum number of guests.
        price_by_night (Integer): The price by night.
        latitude (Float): place's latitude.
        longitude (Float): place's longitude.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """
            get the list of Review instances
            with place_id equals to the current Place.id
            """
            my_reviews = []
            all_instan_reviews = list(models.storage.all(Review).values())
            for rev in all_instan_reviews:
                if rev.place_id == self.id:
                    my_reviews.append(rev)
            return my_reviews
