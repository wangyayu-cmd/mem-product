from django.urls import path

from projects import views

urlpatterns = [
    path('get/',views.get_project),
    path('create/',views.create_project),
]