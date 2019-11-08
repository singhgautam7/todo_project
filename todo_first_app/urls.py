from django.urls import path
from todo_first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross/<list_id>', views.cross, name="cross"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/', views.edit, name="edit"),
    path('<temp>', views.filtering, name="filtering"),
]
