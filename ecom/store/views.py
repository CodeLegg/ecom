from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Collection, Product  # Ensure correct import


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def wholesale(request):
    return render(request, 'wholesale.html', {})

def collections(request, slug=None):
    collection = None
    products = None
    
    # Try to get the "CBD Packaging" collection
    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")
    
    # Get collections that are children of "CBD Packaging"
    collections = Collection.objects.filter(parent=cbd_packaging)
    
    # Redirect to home if the requested collection slug is "cbd-packaging"
    if slug and slug.lower() == "cbd-packaging":
        return redirect('collections')

    if slug:
        try:
            collection = get_object_or_404(Collection, slug=slug)
            products = collection.products.filter(is_active=True)
        except Collection.DoesNotExist:
            messages.error(request, "That Collection Doesn't Exist.")
            return redirect('collections')

    context = {
        'collection': collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'collections.html', context)

def collection_detail(request, slug):
    # Try to get the "CBD Packaging" collection
    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")
    
    # Redirect if the slug is "cbd-packaging"
    if slug.lower() == "cbd-packaging":
        return redirect('collections')
    
    # Get the collection based on the slug
    collection = get_object_or_404(Collection, slug=slug)
    
    # Get all products associated with the collection
    products = Product.objects.filter(collection=collection)
    
    context = {
        'collection': collection,
        'products': products,
    }
    return render(request, 'collection_detail.html', context)


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})