from django.urls import path
from .views import weigth_converter, home


urlpatterns = [
    path('', home, name='home'),
    path('weight_converter/', weigth_converter, name='weight_converter'),
]
