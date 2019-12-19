from django.urls import path
from .views import crawler

# Custom urls here
urlpatterns = [
    path('<str:value>', crawler)
]
