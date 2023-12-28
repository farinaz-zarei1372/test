from rest_framework import serializers

from .models import Product, ProductItem, ProductItemTransition


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="item_id")

    class Meta:
        model = ProductItem
        fields = ["id", "product_id", "quantity"]

    def validate(self, attrs):
        if not Product.objects.filter(id=attrs["item_id"]).exists():
            raise serializers.ValidationError("product with this id does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        self.instance = ProductItem.objects.create(item_id=validated_data["item_id"],
                                                   quantity=validated_data["quantity"])
        return self.instance


class SimpleProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ["id", "quantity"]


class ProductItemTransitionSerializer(serializers.ModelSerializer):
    product_item_id = serializers.IntegerField(write_only=True)
    product_item = SimpleProductItemSerializer(read_only=True)

    class Meta:
        model = ProductItemTransition
        fields = ["id", "product_item", "product_item_id", "status", "transition_time"]

    def validate(self, attrs):
        if not ProductItem.objects.filter(id=attrs["product_item_id"]).exists():
            raise serializers.ValidationError("product item with this id does not exists")
        if attrs["status"] == "EXPORT":
            if ProductItem.objects.get(id=attrs["product_item_id"]).quantity == 0:
                raise serializers.ValidationError("quantity of this item is zero!")
        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data["status"] == "IMPORT":
            item = ProductItem.objects.get(item_id=validated_data["product_item_id"])
            item.quantity += 1
            item.save()
        else:
            item = ProductItem.objects.get(item_id=validated_data["product_item_id"])
            item.quantity -= 1
            item.save()
        self.instance = ProductItemTransition.objects.create(**validated_data)
        return self.instance
