#!/usr/bin/python3

from ..persistence.repository import InMemoryRepository
from ..models import Amenity, User, Place, Review

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
    
    def create_place(self, place_data):
        owner = self.user_repo.get(place_data['owner_id'])
        if not owner:
            raise ValueError("Owner does not exist")
        
        if place_data['price'] <= 0:
            raise ValueError("Price must be a positive value.")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner  # Link the owner to the place
        )
        
        amenity_ids = place_data.get('amenity_ids', [])
        for amenity_id in amenity_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                place.amenities.append(amenity)
                
        self.place_repo.add(place)
        return (place)

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID '{place_id}' not found.")
        
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [{'id': a.id, 'name': a.name} for a in place.amenities]
        }
        
    def get_all_places(self):
        places = self.place_repo.get_all()
        return [{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name
            },
            'amenities': [{'id': a.id, 'name': a.name} for a in place.amenities]
        } for place in places]

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID '{place_id}' not found.")

        # Update attributes if provided
        if 'title' in place_data:
            place.title = place_data['title']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'price' in place_data:
            if place_data['price'] <= 0:
                raise ValueError("Price must be a positive value.")
            place.price = place_data['price']
        if 'latitude' in place_data:
            if not (-90 <= place_data['latitude'] <= 90):
                raise ValueError("Latitude must be between -90 and 90.")
            place.latitude = place_data['latitude']
        if 'longitude' in place_data:
            if not (-180 <= place_data['longitude'] <= 180):
                raise ValueError("Longitude must be between -180 and 180.")
            place.longitude = place_data['longitude']

        # Handle amenities if provided
        if 'amenity_ids' in place_data:
            place.amenities.clear()
            for amenity_id in place_data['amenity_ids']:
                amenity = self.amenity_repo.get(amenity_id)
                if amenity:
                    place.amenities.append(amenity)

        # Save the updated place
        self.place_repo.update(place_id, place)
        return place
    
    def create_review(self, review_data):
        user = self.user_repo.get(review_data['user_id'])
        if not user:
            raise ValueError("User does not exist.")
        
        place = self.place_repo.get(review_data['place_id'])
        if not place:
            raise ValueError("Place does not exist.")
        
        if not (1 <= review_data['rating'] <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        if 'text' not in review_data or not review_data['text']:
            raise ValueError("Review text is required.")
        
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place=place,
            user=user
        )
        
        
        self.review_repo.add(review)
        place.add_review(review)  
        self.place_repo.update(place.id, place)
        
        return (review)
        
    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID '{review_id}' not found.")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID '{place_id}' not found.")
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID '{review_id}' not found.")

        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data and 1 <= review_data['rating'] <= 5:
            review.rating = review_data['rating']
        else:
            raise ValueError("Rating must be between 1 and 5.")
        
        self.review_repo.update(review_id, review)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID '{review_id}' not found.")
        
        # Remove the review from the place
        place = review.place
        place.reviews.remove(review)
        self.place_repo.update(place.id, place)
        
        # Delete the review from the repository
        self.review_repo.delete(review_id)
        return f"Review {review_id} deleted successfully."