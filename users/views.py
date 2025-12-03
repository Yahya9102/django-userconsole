from django.shortcuts import render, redirect, get_object_or_404
from .services import add_user, list_users, delete_user, update_user
from .models import User

# Create your views here.


def user_create(request):

    if request.method == "POST":
        name = request.POST.get("name", "")
        success, msg = add_user(name)

        if success:
            return redirect(f"/users/?message={msg}")
        else:
            context = {
                "title": "Skapa ny användare",
                "error": msg,
                "name_value": name,
            }
            return render(request, "users/user_form.html", context)
    
    context = {
        "title": "Skapa ny användare",
        "name_value": "",
    }
    return render(request, "users/user_form.html", context)


def user_list(request):

    users = list_users()
    message = request.GET.get("message")
    
    context = {
        "users": users,
        "message": message,
    }
    return render(request, "users/user_list.html", context)

def user_update(request, user_id):

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        
        new_name = request.POST.get("name", "")
        
        success, msg = update_user(user_id, new_name)

        if success: 
            return redirect(f"/users/?message={msg}")
        else:
              context = {
                "title": "Uppdatera användare",
                "error": msg,
                "name_value": new_name,
            }
        return render(request, "users/user_form.html", context)
    
    context = {
        "title": "Uppdatera användare",
        "name_value": user.name,
    }
    return render(request, "users/user_form.html", context)


def user_delete(request, user_id):
    
    user = get_object_or_404(User, id=user_id)


    if request.method == "POST":
        success, msg = delete_user(user_id)
        return redirect(f"/users/?message={msg}")
    

    context = {
        "user": user,
    }
    return render(request, "users/user_confirm_delete.html", context)