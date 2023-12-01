
from django.contrib import admin
from django.urls import path
from app.views import age_in, hello_view, burger_view

urlpatterns = [
    path('burger-place', burger_view, name='burger'),
    path('hello-user', hello_view, name='hello-user'),
    path('age-in', age_in, name='age-in'),
    path('admin/', admin.site.urls),
]
