from django.contrib import admin
from django.urls import path,include
from delivery import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

api_description = """
The Food Delivery API provides endpoints for calculating delivery costs for different types of food items across various zones based on distance and item type. 

<b>Sample Data</b> (Not the actual schema)

<table>
    <tr>
        <td><b>Organization ID</b></td>
        <td><b>Name</b></td>
        <td><b>Zone</b></td>
        <td><b>Item Type</b></td>
        <td><b>Per KM price</b></td>
        <td><b>Fixed Price</b></td>
        <td><b>Base Price</b></td>
    </tr>
    <tr>
        <td>1</td>
        <td>Google</td>
        <td>central</td>
        <td>perishable</td>
        <td>1.5</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Google</td>
        <td>central</td>
        <td>non_perishable</td>
        <td>1</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Apple</td>
        <td>north</td>
        <td>perishable</td>
        <td>1.5</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Apple</td>
        <td>north</td>
        <td>non_perishable</td>
        <td>1</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Microsoft</td>
        <td>south</td>
        <td>perishable</td>
        <td>2</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Microsoft</td>
        <td>south</td>
        <td>non_perishable</td>
        <td>1.5</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Viga</td>
        <td>east</td>
        <td>perishable</td>
        <td>2</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Viga</td>
        <td>east</td>
        <td>non_perishable</td>
        <td>1.5</td>
        <td>10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Amazon</td>
        <td>west</td>
        <td>perishable</td>
        <td>1</td>
        <td>20</td>
        <td>10</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Amazon</td>
        <td>west</td>
        <td>non_perishable</td>
        <td>1</td>
        <td>20</td>
        <td>10</td>
    </tr>    
</table>

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
