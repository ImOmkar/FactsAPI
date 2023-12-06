from rest_framework import serializers
from .models import Facts


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facts
        fields = "__all__"