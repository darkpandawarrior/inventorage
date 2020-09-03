from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('add_newTransaction',views.add_newTransaction, name='add_newTransaction'),
    path('update_inventoryItem',views.update_inventoryItem, name='update_inventoryItem'),
    path('add_newItem',views.add_newItem, name='add_newItem'),
    path('low_Items',views.low_Items, name='low_Items'),
    path('view_stockItem',views.view_stockItem, name='view_stockItem'),
    path('view_transactions',views.view_transactions, name='view_transactions'),
    path('import_itemDataSet',views.import_itemDataSet, name='import_itemDataSet'),
    path('clear_database',views.clear_database, name='clear_database'),
    path('about_us',views.about_us, name='about_us'),
    path('delete_item',views.delete_item, name='delete_item'),
]