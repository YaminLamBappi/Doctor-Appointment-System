# myproject/urls.py
from django.urls import path
from . import views
from users.views import (login_view,logout_view, sign_up)


urlpatterns = [
    path('', login_view),
    path('logout/', logout_view),
    path('signup/', sign_up, name='signup'),
    path('home/', views.home, name='home'), 
    ]
