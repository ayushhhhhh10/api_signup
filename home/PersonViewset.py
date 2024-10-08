from rest_framework import viewsets
from .models import Person
from .PersonSerializer import PersonSerializer
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer