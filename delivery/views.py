from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .services import PriceCalculator
from .serializers import DeliveryPriceSerializer


class CalculateDeliveryPrice(GenericAPIView): 
    """
    API endpoint to calculate delivery costs for different types of food items across various zones based on the distance and item type.
    """
    serializer_class = DeliveryPriceSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        
        zone = validated_data.get('zone')
        organization_id = validated_data.get('organization_id')
        total_distance = validated_data.get('total_distance')
        item_type = validated_data.get('item_type')

        total_price = PriceCalculator.calculate_price(zone, organization_id, total_distance, item_type)

        if total_price is not None:
            return Response({'total_price': total_price}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Pricing not found for given inputs'}, status=status.HTTP_400_BAD_REQUEST)
