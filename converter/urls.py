from django.urls import path
from .views import converter, home


urlpatterns = [
    path('', home, name='home'),
    path('converter/', converter, name='converter'),
]
