from django.urls import path
from .views import CR,Regiter ,Login, Operations, BdTeam
urlpatterns = [
    path('general/', CR.as_view()),
    path('register/', Regiter.as_view()),
    path('login/', Login.as_view()),
    path('operation/', Operations.as_view()),
    path('BD/<id>', BdTeam.as_view()),
    
]
