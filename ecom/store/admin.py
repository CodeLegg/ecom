from django.contrib import admin
from .models import Collection, Customer, Product, Order, ProductCollection
from django.utils.text import slugify
from mptt.admin import MPTTModelAdmin

# Inline for ProductCollection to manage products in the Collection
class ProductCollectionInline(admin.TabularInline):
    model = ProductCollection
    extra = 1  # Show one extra blank form
    fields = ['product', 'order']
    ordering = ['order']


class CollectionAdmin(MPTTModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'is_featured', 'order', 'parent')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'is_featured', 'parent')

    # Make 'order' editable directly in the list view
    list_editable = ('order',)

    # Use MPTT to order nodes according to the tree structure
    mptt_level_indent = 20  # Indent children by 20 pixels in admin view

    # Optional: Group fields and customize the form layout
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'image', 'is_active', 'is_featured', 'order', 'parent')
        }),
        ('Visibility Dates', {
            'fields': ('visible_from', 'visible_to')
        }),
        ('Timestamps', {
            'fields': ('updated_at',)
        }),
    )
    readonly_fields = ('updated_at',)

    # Add the ProductCollection inline to manage products in the collection
    inlines = [ProductCollectionInline]

    # Enforce slug generation
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

    # Provide custom ordering in the list view
    ordering = ['tree_id', 'lft']  # Tree-specific ordering to maintain hierarchy



# Register your models here.
# Register models with their respective admins
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)