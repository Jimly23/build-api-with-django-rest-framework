from .models import Kontak
from rest_framework import serializers
    
class KontakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontak
        fields = '__all__'