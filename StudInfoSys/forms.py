from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:

        model = Supplier
        fields = [
            'sname', 'item', 'phone_prefix', 'contact_number', 
            'contact_email', 'status', 'contact_person', 
            'address', 'zip_code', 'barangay_number'
        ]
        widgets = {
            'sname': forms.TextInput(attrs={'id': 'supplierName'}),
            'item': forms.Select(attrs={'id': 'item'}, choices=[('Item1', 'Item1'), ('Item2', 'Item2')]),  # Add item choices
            'phone_prefix': forms.Select(attrs={'id': 'phonePrefix'}, choices=[('+63', '+63'), ('+1', '+1')]),  # Add phone prefixes
            'contact_number': forms.TextInput(attrs={'id': 'phoneNumber'}),
            'contact_email': forms.EmailInput(attrs={'id': 'emailAddress'}),
            'status': forms.Select(attrs={'id': 'status'}, choices=[('Active', 'Active'), ('Inactive', 'Inactive')]),
            'contact_person': forms.TextInput(attrs={'id': 'contactPerson'}),
            'address': forms.TextInput(attrs={'id': 'address'}),
            'zip_code': forms.TextInput(attrs={'id': 'zipCode'}),
            'barangay_number': forms.TextInput(attrs={'id': 'barangayNumber'}),
        }
