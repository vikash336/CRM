from django.urls import path
from .views import CR,Regiter ,Login
urlpatterns = [
    path('general/', CR.as_view()),
    path('register/', Regiter.as_view()),
    path('login/', Login.as_view())
]
