
from django.contrib import admin
from django.urls import path
from app.models import Contact

urlpatterns = [
    path('admin/', admin.site.urls),
]
