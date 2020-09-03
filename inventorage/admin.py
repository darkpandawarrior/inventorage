from django.contrib import admin
from .models import items_inv,transactions_inv


# Register your models here.
admin.site.register(items_inv)
admin.site.register(transactions_inv)
