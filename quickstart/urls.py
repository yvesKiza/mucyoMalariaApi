from django.urls import path
from quickstart import views

urlpatterns = [
    
    path('predict/', views.predict.as_view())
]