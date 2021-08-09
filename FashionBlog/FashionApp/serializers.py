from django.db import models
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'product_tag',
            'category',
            'status',
            'stock',
            'price',
            'image_url',
            'date_posted',
            'colour'
        )
        model = Product