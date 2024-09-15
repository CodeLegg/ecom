from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Collection, Product  # Ensure correct import


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def wholesale(request):
    return render(request, 'wholesale.html', {})

def collections(request, slug=None):
    # Initialize variables
    collection = None
    products = None
    collections = Collection.objects.exclude(name="CBD Packaging")  # Exclude the specific Collection

     # Redirect to home if the requested collection is "CBD Packaging"
    if slug == "cbd-packaging":  # Assuming 'slug' is in a URL-friendly format
        return redirect('collections')  # Redirect to the home page

    if slug:
        try:
            # Look up the Collection by slug
            collection = get_object_or_404(Collection, slug=slug)
            # Get all products directly related to this Collection
            products = collection.products.filter(is_active=True)
        except Collection.DoesNotExist:
            # Handle the case where the Collection does not exist
            messages.error(request, "That Collection Doesn't Exist.")
            return redirect('collections')  # Redirect to the collection list if Collection doesn't exist

    context = {
        'collection': collection,
        'collections': collections,  # List all collections excluding "CBD PACKAGING"
        'products': products,  # Products for a specific Collection
    }

    return render(request, 'collections.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Collection, Product

def collection_detail(request, slug):
    # Get the collection based on the slug
    collection = get_object_or_404(Collection, slug=slug)
    
    # Get all products associated with the collection
    products = Product.objects.filter(collection=collection)
    
    context = {
        'collection': collection,
        'products': products,
    }
    
    return render(request, 'collection_detail.html', context)
