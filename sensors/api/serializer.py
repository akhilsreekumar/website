from rest_framework import serializers
from ..models import Temper

class TemperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Temper
		fields = '__all__'