from .models import Pricing
from decimal import Decimal

class PriceCalculator:
    @staticmethod
    def calculate_price(zone, organization_id, total_distance, item_type):
        
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            item__type=item_type,
            zone=zone
        ).first()

        if not pricing:
            return None
        
        base_distance = pricing.base_distance_in_km
        base_price = pricing.fix_price
        per_km_price = pricing.km_price

        if total_distance <= base_distance:
            total_price = base_price
        else:
            extra_distance = total_distance - base_distance
            total_price = base_price + Decimal(extra_distance) * per_km_price

        return total_price

