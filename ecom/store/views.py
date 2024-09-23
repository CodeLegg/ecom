from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Collection, Product  # Ensure correct import


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def wholesale(request):
    return render(request, 'wholesale.html', {})

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Collection, Product


def sticker_collections(request, slug=None):
    collection = None
    products = None

    # Try to get the "Stickers, Labels, Design & Print" collection
    stickers_collection = get_object_or_404(Collection, name="Stickers, Labels, Design & Print")

    # Get collections that are children of "Stickers, Labels, Design & Print"
    collections = Collection.objects.filter(parent=stickers_collection)

    # Redirect to home if the requested collection slug is "stickers-labels-design-print"
    if slug and slug.lower() == "stickers-labels-design-print":
        return redirect('sticker_collections')

    if slug:
        try:
            collection = get_object_or_404(Collection, slug=slug)
            products = Product.objects.filter(
                product_collections__in=collection.get_descendants(include_self=True),
                is_active=True
            ).distinct()        
        
        except Collection.DoesNotExist:
            messages.error(request, "That Collection Doesn't Exist.")
            return redirect('sticker_collections')
        else:
        # Return products from the parent collection and all its child collections
            products = Product.objects.filter(
            product_collections__in=collections,
            is_active=True
        ).distinct()

    context = {
        'collection': collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'sticker_collections.html', context)

def sticker_sub_collections_list(request, slug):
    collection = get_object_or_404(Collection, slug=slug)
    # Adjust the attribute to 'children' to reflect the model's related_name
    sub_collections = collection.children.all()

    return render(request, 'sub_collections_list.html', {
        'collection': collection,
        'sub_collections': sub_collections
    })

def sticker_sub_collections_product_list(request, slug):
    try:
        sub_collection = Collection.objects.get(slug=slug)  # Getting the specific sub-collection by slug
        # Use the ManyToManyField `product_collections` to filter products
        products = Product.objects.filter(product_collections=sub_collection, is_active=True)  
    except Collection.DoesNotExist:
        sub_collection = None
        products = []

    return render(request, 'sub_collections_product_list.html', {
        'sub_collection': sub_collection,
        'products': products
    })


def sticker_collections_product_list(request, slug):
    # Try to get the "Stickers, Labels, Design & Print" collection
    stickers_collection = get_object_or_404(Collection, name="Stickers, Labels, Design & Print")

    # Get the collection based on the slug
    collection = get_object_or_404(Collection, slug=slug)
    
    # Check if the collection has the correct parent
    if collection.parent != stickers_collection:
        messages.error(request, "That Collection is not part of the 'Stickers, Labels, Design & Print' collection.")
        return redirect('sticker_collections')
    
    # Get products from the current collection and all of its sub-collections
    products = Product.objects.filter(
        product_collections__in=collection.get_descendants(include_self=True),
        is_active=True
    ).distinct()

    context = {
        'collection': collection,
        'products': products,
    }

    return render(request, 'sticker_collections_product_list.html', context)




def cbd_collections(request, slug=None):
    collection = None
    products = None

    # Try to get the "CBD Packaging" collection
    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")

    # Get collections that are children of "CBD Packaging"
    collections = Collection.objects.filter(parent=cbd_packaging)

    # Redirect to home if the requested collection slug is "cbd-packaging"
    if slug and slug.lower() == "cbd-packaging":
        return redirect('cbd_collections')

    if slug:
        try:
            collection = get_object_or_404(Collection, slug=slug)
            # Use ManyToManyField to filter products
            products = Product.objects.filter(product_collections=collection, is_active=True)
        except Collection.DoesNotExist:
            messages.error(request, "That Collection Doesn't Exist.")
            return redirect('cbd_collections')

    context = {
        'collection': collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'cbd_collections.html', context)


def cbd_collections_product_list(request, slug):
    # Try to get the "CBD Packaging" collection
    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")

    # Get the collection based on the slug
    collection = get_object_or_404(Collection, slug=slug)

    # Check if the collection has the correct parent
    if collection.parent != cbd_packaging:
        messages.error(request, "That Collection is not part of the 'CBD Packaging' collection.")
        return redirect('cbd_collections')

   # Use ManyToManyField to filter products
    products = Product.objects.filter(product_collections=collection, is_active=True)

    context = {
        'collection': collection,
        'products': products,
    }
    return render(request, 'cbd_collections_product_list.html', context)




def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product.html', {'product': product})