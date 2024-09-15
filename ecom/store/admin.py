from django.contrib import admin
from .models import Collection, Customer, Product, Order


# Register your models here.
# Now register models with their respective admins
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)