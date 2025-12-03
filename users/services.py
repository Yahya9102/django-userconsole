from django.db import IntegrityError
from .models import User

def add_user(name: str) -> tuple[bool, str]:
    
    cleaned = name.strip()
    
    if not cleaned:
        return False, "Namnet får inte vara tomt!"
    user = User(name= cleaned)
    try:
        user.save()
        return True, f"Användare '{cleaned}' har skapats!"
    except IntegrityError:
        return False, f"Användare '{cleaned}' finns redan"
