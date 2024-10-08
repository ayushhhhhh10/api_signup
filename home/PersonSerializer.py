from rest_framework import  serializers
from .models import Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','username','first_name','last_name','email','password','otp']
