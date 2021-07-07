from django.urls import path
from .views import weight_converter, home


urlpatterns = [
    path('', home, name='home'),
    path('weight_converter/', weight_converter, name='weight_converter'),
]
