#!/usr/bin/python3

from ..persistence.repository import InMemoryRepository
from ..models.user import User
from ..models import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    
    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
    
    def create_amenity(self, amenity_data):
        if 'name' not in amenity_data or not amenity_data['name']:
            raise ValueError("Amenity name is required.")
        
        existing_amenity = self.amenity_repo.get_by_attribute('name', amenity_data['name'])
        if existing_amenity:
            raise ValueError(f"Amenity with name '{amenity_data['name']} already exists.")
        
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return (amenity)

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError(f"Amenity with ID '{amenity_id} not found.")
        return amenity

    def get_all_amenities(self):
        return (self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        
        if 'name' in amenity_data:
            if not amenity_data['name']:
                raise ValueError("Amenity name cannot be empty")
            
            existing_amenity = self.amenity_repo.get_by_attribute('name', amenity_data['name'])
            if existing_amenity and existing_amenity.id != amenity_id:
                raise ValueError(f"Amenity with name '{amenity_data['name']}' already exists")
        
        amenity.update(**amenity_data)
        self.amenity_repo.update(amenity_id, amenity)
        
        return (amenity)
    
    