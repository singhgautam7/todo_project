from django.contrib import admin
from django.urls import include, path, re_path
from todo_first_app import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', include('todo_first_app.urls')),           #this is the alias of old url() function, and is used to work with regular expressions.
    path('admin/', admin.site.urls),
]
