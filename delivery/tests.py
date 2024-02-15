from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import PriceCalculator

class CalculateDeliveryPriceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_calculate_delivery_price(self):
        data = {
            'zone': 'zone1',
            'organization_id': 1,
            'total_distance': 100,
            'item_type': 'type1'
        }
        response = self.client.post('/api/calculate-delivery-price/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_price', response.data)

    def test_invalid_data(self):
        data = {
            'zone': 'zone1',
            'organization_id': 1,
            'total_distance': -100,  # invalid distance
            'item_type': 'type1'
        }
        response = self.client.post('/api/calculate-delivery-price/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('total_distance', response.data['errors'])

    def test_pricing_not_found(self):
        data = {
            'zone': 'unknown_zone',
            'organization_id': 999,  # unknown organization
            'total_distance': 100,
            'item_type': 'type1'
        }
        response = self.client.post('/api/calculate-delivery-price/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
