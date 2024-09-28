from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Collection, Product  # Ensure correct import
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404
from .models import Collection, Product
from django.shortcuts import redirect


def home(request):
    # Fetch the "Stickers, Labels, Design & Print" and "Pre-Made Sticker Shop" collections
    stickers_collection = get_object_or_404(Collection, name="Stickers, Labels, Design & Print")
    premade_collection = get_object_or_404(Collection, name="Pre-Made Sticker Shop")

    # Fetch child collections for both parent collections
    sticker_subcollections = Collection.objects.filter(parent=stickers_collection)
    premade_subcollections = Collection.objects.filter(parent=premade_collection)
    
    # Combine the collections
    collections = sticker_subcollections | premade_subcollections

    # Slugs of specific products you want to display
    selected_slugs = ['custom-die-cut-stickers', 'colorful-bear', 'the-gay-bear']  # Add your slugs here

    # Filter products by their slugs from both collections and their descendants
    products = Product.objects.filter(
        product_collections__in=stickers_collection.get_descendants(include_self=True) |
                               premade_collection.get_descendants(include_self=True),
        slug__in=selected_slugs,  # Filter products by slug
        is_active=True
    ).distinct()

    # Pass the collections and products to the context
    context = {
        'stickers_collection': stickers_collection,
        'premade_collection': premade_collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'home.html', context)

def wholesale(request):
    return render(request, 'wholesale.html', {})


# STICKER COLLECTIONS VIEWS

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
    # Check if the slug is "pre-made-sticker-shop"
    if slug == "pre-made-sticker-shop":
        # Redirect to the "themes" URL for the same slug
        return redirect('sticker_sub_collections_list', slug=slug)

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

# CBD COLLECTIONS VIEWS

def cbd_section(request):
    return render(request, 'cbd_section.html', {})

def cbd_collections(request, slug=None):
    # Check if age is confirmed
    if not request.session.get('age_confirmed', False):
        return render(request, 'cbd_collections.html', {'show_age_modal': True})

    # The rest of your view logic remains the same
    collection = None
    products = None

    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")
    collections = Collection.objects.filter(parent=cbd_packaging)

    if slug and slug.lower() == "cbd-packaging":
        return redirect('cbd_collections')

    if slug:
        try:
            collection = get_object_or_404(Collection, slug=slug)
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
    # Check if age is confirmed
    if not request.session.get('age_confirmed', False):
        return render(request, 'cbd_collections.html', {'show_age_modal': True})

    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")
    collection = get_object_or_404(Collection, slug=slug)

    if collection.parent != cbd_packaging:
        messages.error(request, "That Collection is not part of the 'CBD Packaging' collection.")
        return redirect('cbd_collections')

    products = Product.objects.filter(product_collections=collection, is_active=True)

    context = {
        'collection': collection,
        'products': products,
    }
    return render(request, 'cbd_collections_product_list.html', context)

@csrf_exempt
def confirm_age(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('age_confirmed', False):
            request.session['age_confirmed'] = True
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product.html', {'product': product})