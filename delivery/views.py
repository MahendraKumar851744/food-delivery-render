from django.http import JsonResponse
from .services import PriceCalculator
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import re

@csrf_exempt
def calculate_delivery_price(request):
    if request.method == 'POST':
        data = request.POST

        if 'zone' not in data or 'organization_id' not in data or 'total_distance' not in data or 'item_type' not in data:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        zone = data.get('zone')
        organization_id = data.get('organization_id')
        total_distance_str = data.get('total_distance')
        item_type = data.get('item_type')
        
        if not re.match(r'^-?\d+(\.\d+)?$', total_distance_str):
            return JsonResponse({'error': 'Invalid total_distance value. Must be a decimal number'}, status=400)

        try:
            total_distance = Decimal(total_distance_str)
        except ValueError:
            return JsonResponse({'error': 'Invalid total_distance value'}, status=400)

        if total_distance <= 0:
            return JsonResponse({'error': 'Total_distance must be a positive number'}, status=400)

        if item_type not in ['perishable', 'non_perishable']:
            return JsonResponse({'error': 'Invalid item_type value. Must be perishable or non_perishable'}, status=400)


        total_price = PriceCalculator.calculate_price(zone, organization_id, total_distance, item_type)

        if total_price is not None:
            return JsonResponse({'total_price': total_price})
        else:
            return JsonResponse({'error': 'Pricing not found for given inputs'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
