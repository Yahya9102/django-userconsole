from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("", views.user_list, name="list"),  #/users/
    path("create/", views.user_create, name="create"), #/users/create/
    path("<int:user_id>/edit", views.user_update, name="update"),
    path("<int:user_id>/delete/", views.user_delete, name="delete")
    
]

