from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.index,name="index"),
    # path("search",views.search,name="search"),
]
