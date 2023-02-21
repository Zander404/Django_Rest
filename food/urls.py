from django.urls import path
from . import views


urlpatterns= [
    path('', views.food_list),
    path('<int:id>', views.food_detail)
] 