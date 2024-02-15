from django.contrib import admin
from django.urls import path,include
from delivery import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

api_description = """
The Food Delivery API provides endpoints for calculating delivery costs for different types of food items across various zones based on distance and item type. 

<p>There are different zones available in the database right now:</p>
    <ul>
        <li>Central</li>
        <li>North</li>
        <li>South</li>
        <li>East</li>
        <li>West</li>
    </ul>

<p>Each have different items types, which can either be perishable or non-perishable.</p>

<p>We also have different organizations in the database:</p>
<ul>
    <li>Organization ID: 1</li>
    <li>Organization ID: 2</li>
    <li>Organization ID: 3</li>
    <li>Organization ID: 4</li>
</ul>

For complete documentation, please visit <a href="http://127.0.0.1:8000/api/v1/documentation/">API Documentation</a>.

    
<b>Test the API</b>

To test the API, you can send a POST request with the following JSON payload:

```json
{
    "zone": "central",
    "organization_id": "1",
    "total_distance": "12",
    "item_type": "perishable"
} 
"""


schema_view = get_schema_view(
   openapi.Info(
      title="Food Delivery API (Dynamic Pricing)",
      default_version='v1',
      description=api_description,
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',
         include([
             path('calculate_delivery_price/', views.CalculateDeliveryPrice.as_view()),
             path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
         ])
        
    )
]
