from django.contrib import admin
from .models import Collection, Customer, Product, Order

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'is_featured', 'order', 'parent')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'is_featured', 'parent')
    filter_horizontal = ('products',)

    # Make 'order' editable directly in the list view
    list_editable = ('order',)
    
    # Optionally, make 'parent' editable in the form and add a custom form layout
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'image', 'is_active', 'is_featured', 'order', 'parent', 'products')
        }),
        ('Dates', {
            'fields': ('visible_from', 'visible_to')
        }),
    )

    # Optionally, provide a custom ordering in the admin list view
    ordering = ['order', 'name']

# Register your models here.
# Now register models with their respective admins
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
