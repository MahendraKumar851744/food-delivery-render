from django.db import models

class Organization(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return  f"{self.name}"

class Item(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f"Item {self.id}"

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=10, decimal_places=2)
    fix_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Org: {self.organization.name}  -  Item: {self.item.id}  -  zone: {self.zone}"
