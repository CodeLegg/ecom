from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Collection, Product  # Ensure correct import
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Helper function to get products by collection and apply the consistent filter logic
def get_ordered_products_by_collection(collection):
    return Product.objects.filter(
        in_collections__collection__in=collection.get_descendants(include_self=True),
        is_active=True
    ).order_by('in_collections__order').distinct()

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

    # Correct the query: Use `in_collections` instead of `product_collections`
    products = Product.objects.filter(
        in_collections__collection__in=stickers_collection.get_descendants(include_self=True) |
                                      premade_collection.get_descendants(include_self=True),
        slug__in=selected_slugs,
        is_active=True
    ).distinct().order_by('in_collections__order')

    # Pass the collections and products to the context
    context = {
        'stickers_collection': stickers_collection,
        'premade_collection': premade_collection,
        'products': products,
                'collections': collections,

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
            products = get_ordered_products_by_collection(collection)
        except Collection.DoesNotExist:
            messages.error(request, "That Collection Doesn't Exist.")
            return redirect('sticker_collections')
    else:
        products = Product.objects.filter(
            in_collections__collection__in=collections,  # Corrected related name
            is_active=True
        ).distinct().order_by('in_collections__order')

    context = {
        'collection': collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'sticker_collections.html', context)

def sticker_collections_product_list(request, slug):
    # Check for extra segments in the URL
    url_parts = request.path.strip('/').split('/')
    
    # If there are more than 3 parts in the URL (e.g., "sticker-collections/slug/extra"), redirect to the correct URL
    if len(url_parts) > 2:
        return redirect('sticker_collections_product_list', slug=slug)

    # Get the Stickers collection
    stickers_collection = get_object_or_404(Collection, name="Stickers, Labels, Design & Print")
    
    # Fetch the collection by slug
    collection = get_object_or_404(Collection, slug=slug)

    # Ensure that the collection is a part of "Stickers, Labels, Design & Print"
    if collection.parent != stickers_collection:
        messages.error(request, "That Collection is not part of the 'Stickers, Labels, Design & Print' collection.")
        return redirect('sticker_collections')

    # Fetch products for the current collection
    products = get_ordered_products_by_collection(collection)

    context = {
        'collection': collection,
        'products': products,
    }

    return render(request, 'sticker_collections_product_list.html', context)


from django.shortcuts import render, get_object_or_404, redirect

def sticker_sub_collections_list(request, slug):
    url_parts = request.path.strip('/').split('/')

    # If the URL has extra segments, remove them and redirect
    if len(url_parts) > 2:  # "sub-sticker-collections/<slug>/themes/"
        clean_url = f'/pre-made-sticker-shop/{slug}/'
        return redirect(clean_url)

    # Fetch the collection by slug
    collection = get_object_or_404(Collection, slug=slug)
    sub_collections = collection.children.all()

    return render(request, 'sub_collections_list.html', {
        'collection': collection,
        'sub_collections': sub_collections
    })


def sticker_sub_collections_product_list(request, slug):
    url_parts = request.path.strip('/').split('/')

    # If the URL has extra segments, remove them and redirect
    if len(url_parts) > 2:  # "pre-made-sticker-shop/theme/<slug>/"
        clean_url = f'/pre-made-sticker-shop/{slug}/'
        return redirect(clean_url)

    # Fetch the collection by slug
    sub_collection = get_object_or_404(Collection, slug=slug)
    products = get_ordered_products_by_collection(sub_collection)

    return render(request, 'sub_collections_product_list.html', {
        'sub_collection': sub_collection,
        'products': products
    })



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
        collection = get_object_or_404(Collection, slug=slug)
        products = get_ordered_products_by_collection(collection)

    context = {
        'collection': collection,
        'collections': collections,
        'products': products,
    }

    return render(request, 'cbd_collections.html', context)


def cbd_collections_product_list(request, slug):
    # Check for extra segments in the URL
    url_parts = request.path.strip('/').split('/')
    
    # If there are more than 2 parts in the URL (e.g., "cbd-collections/slug/extra"), redirect to the correct URL
    if len(url_parts) > 2:
        return redirect('cbd_collections_product_list', slug=slug)

    # Check if age is confirmed
    if not request.session.get('age_confirmed', False):
        return render(request, 'cbd_collections.html', {'show_age_modal': True})

    # Fetch the CBD Packaging collection
    cbd_packaging = get_object_or_404(Collection, name="CBD Packaging")
    
    # Fetch the collection by slug
    collection = get_object_or_404(Collection, slug=slug)

    # Ensure that the collection is a part of "CBD Packaging"
    if collection.parent != cbd_packaging:
        messages.error(request, "That Collection is not part of the 'CBD Packaging' collection.")
        return redirect('cbd_collections')

    # Fetch products for the current collection
    products = get_ordered_products_by_collection(collection)

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
    # Check for extra segments in the URL
    url_parts = request.path.strip('/').split('/')
    
    # If there are more than 2 parts in the URL (e.g., "product/slug/extra"), redirect to the correct URL
    if len(url_parts) > 2:
        return redirect('product', slug=slug)

    # Fetch the product by slug
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product.html', {'product': product})
