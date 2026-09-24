from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(
        source="vendor_profile.company_name",
        read_only=True
    )
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "price",
            "image",
            "vendor",
            "vendor_profile",
            "vendor_name",
            "category",
            "category_name",
        ]