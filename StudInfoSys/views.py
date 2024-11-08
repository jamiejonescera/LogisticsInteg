from django.shortcuts import render
from .models import Classroom
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_homepage(request):
    return render(request, 'Admin_Home.html')

# Classroom function
def add_inventory(request):
    classrooms = Classroom.objects.all()
    context = {
        "classrooms": classrooms
    }
    return render(request, 'Add_Inv.html', context)


def add_inventory_save(request):
    if request.method != "POST":
        messages.error(request, "Method Not Allowed!")
        return redirect('add_inventory')
    else:
        class_name = request.POST.get('class_name')
        capacity = request.POST.get('capacity')

        try:
            classroom = Classroom (class_name=class_name,
                               capacity=capacity,)          
            classroom.save()
            messages.success(request, "Added Successfully!")
            return redirect('add_inventory')
        except:
            messages.error(request, "Failed to Add!")
            return redirect('add_inventory')




def depreciated_inventory(request):
    return render(request, 'Depreciated_Inv.html')

def depart_inv(request):
    return render(request, 'Depart_Inv.html')

def purchase_request(request):
    return render(request, 'Purchase_Req.html')

def evaluation_request(request):
    return render(request, 'Eval_Req.html')

def add_supplier(request):
    return render(request, 'Add_Supplier.html')

def supplier_list(request):
    return render(request, 'Supplier_List.html')

def edit_supplier(request):
    return render(request, 'Edit_Supplier.html')

def equipment_maintenance(request):
    return render(request, 'Equip_Maintenance.html')

def add_purchase(request):
    return render(request, 'Add_Purch.html')