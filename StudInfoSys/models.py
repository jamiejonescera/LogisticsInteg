from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    sname = models.CharField(max_length=255)  # Supplier Name
    item = models.CharField(max_length=255)  # Selected Item
    phone_prefix = models.CharField(max_length=5, blank=True, null=True)  # Phone Prefix
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Phone Number
    contact_email = models.EmailField(max_length=255, blank=True, null=True)  # Email Address
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])  # Status
    contact_person = models.CharField(max_length=255)  # Contact Person
    address = models.TextField(blank=True, null=True)  # Address (Optional)
    zip_code = models.CharField(max_length=10, blank=True, null=True)  # ZIP Code (Optional)
    barangay_number = models.CharField(max_length=10, blank=True, null=True)  # Barangay Code (Optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.sname
