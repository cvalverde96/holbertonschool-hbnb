#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    def __init__(self):
        # Genera id unico para cada instancia
        self.id = str(uuid.uuid4())
        # Genera timestamp de creacion y update
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def updated_timestamp(self):
        # actualiza updated_at con tiempo actual
        self.updated_at = datetime.now()
        
    def update(self):
        self.update_timestamp()
    
    def __str__(self):
        return (f"BaseModel(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})")
    
    