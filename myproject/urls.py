# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from users.views import (login_view,logout_view, sign_up)

from hospitals.schema import schema  # Import your schema from the correct location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', include('hospitals.urls')),
    path('', login_view),
    path('logout/', logout_view),
    path('signup/', sign_up, name='signup')
    ]
