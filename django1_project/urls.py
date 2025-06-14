
from django.contrib import admin
from django.urls import path
from my1_application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home)
]
