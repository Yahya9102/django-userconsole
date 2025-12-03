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
    

def list_users():
    return User.objects.all().order_by("name")




def get_user(user_id: int) -> User | None:
    try:
        return User.objects.get(id = user_id)
    except User.DoesNotExist:
        return None




def update_user(user_id: int, new_name: str) -> tuple[bool, str]:

    cleaned = new_name.strip()
    
    if not cleaned:
        return False, "Namnet får inte vara tomt!"
    
    
    user = get_user(user_id)
    if user is None:
        return False, "Användare hittades inte"
    

    if User.objects.filter(name = cleaned).exclude(id=user_id).exists():
        return False, "Användaren finns redan"

    user.name = cleaned
    user.save()
    return True, "användaren sparad"



def delete_user(user_id: int) -> tuple[bool, str]:

    user = get_user(user_id)
    if user is None:
        return False, "Användaren hittades inte"
    
    user.delete()
    return True, "Användaren har tagits bort"