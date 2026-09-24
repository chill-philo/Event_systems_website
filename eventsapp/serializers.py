from rest_framework import serializers
from .models import Service, VendorProfile


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


class VendorProfileSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = VendorProfile
        fields = [
            "id",
            "company_name",
            "phone",
            "description",
            "location",
            "whatsapp",
            "instagram",
            "website",
            "services",
        ]