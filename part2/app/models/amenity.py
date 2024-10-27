#!/usr/bin/python3

from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = self.validate_name(name)
    
        
    @staticmethod
    def validate_name(name: str) -> str:
        if not name or len(name) > 50:
            raise ValueError("Name is required and should be less than or equal to 50 characters.")
        return (name)
    
    class Amenity(BaseModel):
        def update(self, **kwargs):
            super().update()
            self.updated_timestamp()
        
    def __str__(self):
        return (f"Amenity(id={self.id}, name={self.name}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})")
            