from rest_framework import serializers
from fit.models import Fit

class FitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fit
        fields ='__all__'
