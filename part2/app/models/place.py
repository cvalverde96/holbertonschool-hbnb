#!/usr/bin/python3

from base import BaseModel
from user import User


"""
importamos uuid para crear el unique identifier
importamos datetime para tener el tiempo acutal exacto
"""

class Place(BaseModel):
    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: "User", description: str = None):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []
    
    
    """
    metodo estatico que asegura que titilo no este vacio
    y su len no sea mayor de 100 chars
    """   
    @staticmethod
    def validate_title(title: str) -> str:
        if not title or len(title) > 100:
            raise ValueError("Title is required and/or should be less than or equal to 100 characters.")
        return (title)
    
    """
    metodo estatico que asegura que precio debe ser un valor positivo
    """
    @staticmethod
    def validate_price(price: float) -> float:
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return (price)
    
    
    """
    metodo estatico que asegura que latitud este dentro de cierto rango
    """
    @staticmethod
    def validate_latitude(latitude: float) -> float:
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be within the range of -90.0 to 90.0.")
        return (latitude)
    
    
    """
    metodo estatico que asegura que longitud este dentro de cierto rango
    """
    @staticmethod
    def validate_longitude(longitude: float) -> float:
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be within the range of -180.0 to 180.0.")
        return (longitude)
    
    """
    metodo estatico que asegura que owner sea una instancia de User
    """
    @staticmethod
    def validate_owner(owner: "User") -> "User":
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance.")
        return (owner)
    
    
    def add_review(self, review):
        from review import Review
        if isinstance(review, Review):  # Make sure the review passed is of the correct type
            self.reviews.append(review)
        else:
            raise ValueError("Invalid review object")
    """
    metodo para validar los atributes y llama las diferentes funciones de validacion
    """
    def update(self, title: str = None, price: float = None, latitude: float = None, longitude: float = None, description: str = None, owner: "User" = None):
        if title:
            self.title = self.validate_title(title)
        if price:
            self.price = self.validate_price(price)
        if latitude:
            self.latitude = self.validate_latitude(latitude)
        if longitude:
            self.longitude = self.validate_longitude(longitude)
        if description:
            self.description = description
        if owner:
            self.owner = self.validate_owner(owner)
        # para actualizar el timestamp de updated_at
        super().update()
    
    
        def __str__(self):
            return (f"Place(id={self.id}, title={self.title}, description={self.description}, "
                f"price={self.price}, latitude={self.latitude}, longitude={self.longitude}, "
                f"owner={self.owner.first_name} {self.owner.last_name}, created_at={self.created_at}, updated_at={self.updated_at})")

        
        