#!/usr/bin/python3

from base import BaseModel
from place import Place
from user import User

"""
importamos uuid para crear el unique identifier
importamos datetime para tener el tiempo exacto
"""


class Review:
    # metodo constructor inicializando los atributos
    def __init__(self, text: str, rating: int, place: "Place", user: "User"):
        super().__init__()
        # atributos que llaman a sus respectivos validates para tener formato correcto
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)
        # atributo para tener tiempo acutal en creacion/y update
    
    """
    metodo estatico para validar que en efecto se este poniendo texto en review
    """
    @staticmethod
    def validate_text(text: str) -> str:
        if not text:
            raise ValueError("Text required")
        return (text)
    
    
    """
    metodo estatico para validar que rating sea entre 1 y el 5
    """
    @staticmethod
    def validate_rating(rating: int) -> int:
        if not (1 <= rating <= 5):
            raise ValueError("Rating given to the place, must be between 1 and 5.")
        return (rating)
    
    
    """
    metodo estatico para validar que se este entrando una instancia valida de Place
    """
    @staticmethod
    def validate_place(place: "Place") -> "Place":
        if not isinstance(place, Place):
            raise ValueError("Must be a valid Place instance")
        return (place)
    
    
    """
    metodo estatico para validar que se este entrando una instancia valida de User
    """
    @staticmethod
    def validate_user(user: "User") -> "User":
        if not isinstance(user, User):
            raise ValueError("Must be a valid User instance")
        return (user)
    
    """
    metodo updata para poder actutalizar la infromatcion del review
    validaciones de if statements del texto y rating
    """
    def update(self, text: str = None, rating: int = None):
        if text:
            self.text = self.validate_text(text)
        if rating:
            self.rating= self.validate_rating(rating)
        super().update()
    
    def __str__(self):
        return (f"Review(id={self.id}, text={self.text}, rating={self.rating}, "
                f"place={self.place.title}, user={self.user.first_name} {self.user.last_name}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})")