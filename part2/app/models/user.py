#!/usr/bin/python3

from base import BaseModel
import re
"""
importamos uuid para generar Universally Unique Identifiers para los usuarios
importamos datetime para guardar cuando se crearon y fueron updated los usuarios
importamos re para validar los formatos de email
"""

class User(BaseModel):
    # metodo constructor inicializando los atributos
    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        
    
    
    """
    metodo estatico validate_name
    para validar que nombre tenga valor/no este vacio
    y que se largo no sea mayor de 50 chars
    """
    @staticmethod
    def validate_name(name: str) -> str:
        if not name or len(name) > 50:
            raise ValueError("Name is required and/or maximum length is of 50 characters")
        return (name)
    
    """
    metodo estatico validate_email
    para validar que email tenga formato requerido
    """
    @staticmethod
    def validate_email(email : str) -> str:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            raise ValueError("Email is required and/or format is invalid")
        return (email)
    
    
    """
    metodo para actualizar los datos de los usuarios
    cada if es para validar que el formateo este correcto
    y luego actualizarlo
    """
    def update(self, first_name=None, last_name= None, email= None, is_admin= None):
        if first_name:
            self.first_name = self.validate_name(first_name)
        if last_name:
            self.last_name = self.validate_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if is_admin is not None:
            self.is_admin = is_admin
        super().update()
        
    # funcion para imprimir info    
    def __str__(self):
        return (f"User(id={self.id}, first_name={self.first_name}, "
                f"last_name={self.last_name}, email={self.email}, "
                f"is_admin={self.is_admin}, created_at={self.created_at}, updated_at={self.updated_at})")