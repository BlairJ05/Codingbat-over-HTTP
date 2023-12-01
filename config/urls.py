
from django.contrib import admin
from django.urls import path
from app.views import front_times, centered_average, xyz_there, no_teen_sum

urlpatterns = [
    path('warmup-2/font-times/', front_times, name="front-times"),
    path('logic-2/no-teen-sum/', no_teen_sum, name="no-teen-sum"),
    path('string-2/xyz-there/', xyz_there, name="xyz-there"),
    path('list-2/centered-average/', centered_average, name="centered-average"),
    path('admin/', admin.site.urls),
]
