from rest_framework import serializers
from . models import satellite

class satelliteSerializers(serializers.ModelSerializer):
	class Meta:
		model=satellite
		fields='__all__'