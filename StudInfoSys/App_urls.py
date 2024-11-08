from django.urls import path #If maging sabaw ka self locate mo sa views.py -CIMC
from . import views  # Ensure to import your views

# URL CONFIGURATION
urlpatterns = [
    path('', views.admin_homepage),
    path('Admin_Home.html', views.admin_homepage),
    path('Add_Inv.html', views.add_inventory),
    path('Depreciated_Inv.html', views.depreciated_inventory),
    path('Depart_Inv.html', views.depart_inv),
    path('Purchase_Req.html', views.purchase_request),
    path('Eval_Req.html', views.evaluation_request),
    path('Add_Supplier.html', views.add_supplier),
    path('Supplier_List.html', views.supplier_list),
    path('Equip_Maintenance.html', views.equipment_maintenance),
    path('Edit_Supplier.html', views.edit_supplier),
    path('Add_Purch.html', views.add_purchase),  # New path added here
]
