# hospitals/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Hospital

class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital

class Query(graphene.ObjectType):
    hospitals = graphene.List(HospitalType)

    def resolve_hospitals(self, info):
        return Hospital.objects.all()

schema = graphene.Schema(query=Query)
