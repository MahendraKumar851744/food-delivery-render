from rest_framework import serializers

class DeliveryPriceSerializer(serializers.Serializer):
    zone = serializers.CharField()
    organization_id = serializers.CharField()
    total_distance = serializers.DecimalField(max_digits=10, decimal_places=2)
    item_type = serializers.ChoiceField(choices=['perishable', 'non_perishable'])
    
    def validate_total_distance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Total_distance must be a positive number")
        return value