from rest_framework   import serializers

from .models          import(
    Image,
    Product,
    Order
)
from user.serailizers import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Image
        fields  = '__all__'
        exclude = ('is_deleted',)

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model   = Product
        fields  = '__all__'
        exclude = ('is_deleted',)

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    user    = UserSerializer(many=True, read_only=True)

    class Meta:
        model   = Order
        fields  = '__all__'
        exclude = ('is_deleted',)
