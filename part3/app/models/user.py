#!/usr/bin/python3

from app.models.base import BaseModel
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt()

class User(BaseModel):

    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.hash_password(password)
        self.is_admin = is_admin
    
    @staticmethod
    def validate_name(name: str) -> str:
        if not name or len(name) > 50:
            raise ValueError("Name is required and/or maximum length is of 50 characters")
        return (name)
    
    @staticmethod
    def validate_email(email : str) -> str:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            raise ValueError("Email is required and/or format is invalid")
        return (email)
    
    def hash_password(self, password: str):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password: str) -> bool:
        return (bcrypt.check_password_hash(self.password, password))
        
    def update(self, first_name=None, last_name=None, email=None, password=None, is_admin=None):
        if first_name:
            self.first_name = self.validate_name(first_name)
        if last_name:
            self.last_name = self.validate_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if password:
            self.hash_password(password)
        if is_admin is not None:
            self.is_admin = is_admin
        super().update()
   
    def __str__(self):
        return (f"User(id={self.id}, first_name={self.first_name}, "
                f"last_name={self.last_name}, email={self.email}, "
                f"is_admin={self.is_admin}, created_at={self.created_at}, updated_at={self.updated_at})")