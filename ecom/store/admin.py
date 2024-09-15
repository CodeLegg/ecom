from django.contrib import admin
from .models import Collection, Customer, Product, Order

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'is_featured', 'order')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'is_featured')
    filter_horizontal = ('products',)  # Add this line to manage the products many-to-many field


# Register your models here.
# Now register models with their respective admins
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
