from django.urls import path


from drink import views

urlpatterns = [
    path('',views.drink_list),
    path('<int:id>', views.drink_detail),
]