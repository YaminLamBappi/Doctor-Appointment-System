# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

from hospitals.schema import schema  # Import your schema from the correct location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', include('hospitals.urls')),
    path('', include('users.urls')),
    path('', include('doctors.urls')),

    ]
