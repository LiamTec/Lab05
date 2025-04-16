from django.shortcuts import render
from .models import BookInventory

def inventory_list(request):
    """View to list all books in inventory"""
    inventory = BookInventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})

def inventory_detail(request, pk):
    """View to show details of a specific book in inventory"""
    book_inventory = BookInventory.objects.get(pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'book_inventory': book_inventory})
