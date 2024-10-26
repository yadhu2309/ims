from rest_framework import serializers

from .models import Product, Supplier, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('total_price',)

    def create(self, validated_data):
        # try:
        print(validated_data['product'].price)
        #     product = Product.objects.get(id=validated_data['product'])
        # except:
        #     raise serializers.ValidationError({'product':'Product not found'})
        validated_data['total_price'] = validated_data['product'].price * validated_data['quantity']
        order = Order.objects.create(**validated_data)
        return order
    

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSupplierSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        