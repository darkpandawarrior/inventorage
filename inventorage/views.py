from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django import forms
from .DB_access import *
# Create your views here.

def index(request):
    low_item = lowQItem().count()
    last_trn = getTransactionsTable()
    count = last_trn.count()
    last_trn = last_trn.reverse()[count-5:count]
    context = {
        'low_item' : low_item,
        'last_trn' : last_trn
    }
    return render(request, "index.html", context)

def add_newTransaction(request):
    if request.method == "POST":
        form = addTransaction(request.POST)

        if form.is_valid():
            id = form.cleaned_data['ItmID_inv']
            discount = form.cleaned_data['Discount_inv']
            date = form.cleaned_data['Date_inv']
            quantity = form.cleaned_data['ImtQnt_inv']
            if createTransaction(id, discount, date, quantity):
                return redirect('index')
            else :
                context = {
                    'form' : form,
                    'error': "Quantity exceeds stock or Invalid Date"
                }
                return render(request, "add_newTransaction.html" , context)

            form.save()
            return redirect('index')

    else:
        form = addTransaction()
        context = {
                    'form' : form,
                    'error': ""
                }
    return render(request, "add_newTransaction.html" , context)

def update_inventoryItem(request):
    if request.method == "POST":
        form = updateInv(request.POST)

        if form.is_valid():
            itemID = form.cleaned_data['ItmID_inv']
            quantity = form.cleaned_data['quantity']
            CP = form.cleaned_data['Cost_price']
            SP = form.cleaned_data['Selling_price']
            if updateItem(itemID, quantity, CP, SP):
                context = {
                    'form' : form,
                    'error': "Item Added Successfully.",
                    'Note' : "Enter Cost Price and Selling Price only to alter previous values"
                }
            else:
                context = {
                    'form' : form,
                    'error': "Item ID not matched!",
                    'Note' : "Enter Cost Price and Selling Price only to alter previous values"
                }
            return render(request, "update_inventoryItem.html", context)

    else:
        form = updateInv()

    context = {
            'form' : form,
            'error': "",
            'Note' : "Enter Cost Price and Selling Price only to alter previous values"
            }
    return render(request, "update_inventoryItem.html", context)

def add_newItem(request):
    if request.method == "POST":
        form = addItemForm(request.POST)

        if form.is_valid():
            itemID = form.cleaned_data['itemsID_inv']
            description = form.cleaned_data['itemsDesc_inv']
            quantity = form.cleaned_data['itemsQnt_inv']
            CP = form.cleaned_data['itemsCostPrice_inv']
            SP = form.cleaned_data['itemsSellPrice_inv']
            if createItem(itemID, description, quantity, CP, SP):
                return redirect('index')
            else:
                context = {
                    'form' : form,
                    'error': " Quantity exceeds stock"
                }
                return render(request, "add_newItem.html", context)

    else:
        form = addItemForm()
        context = {
                    'form' : form,
                    'error': " "
                }
        return render(request, "add_newItem.html", context)
    

def low_Items(request):
    item_set = lowQItem()
    return render(request, "view_stockItem.html", {'item_set':item_set})

def view_stockItem(request):
    item_set = getItemTable()
    return render(request, "view_stockItem.html", {'item_set':item_set})

def view_transactions(request):
    transaction_set = getTransactionsTable()
    return render(request, "view_transactions.html", {'transaction_set' : transaction_set})

def import_itemDataSet(request):
    return render(request, "import_itemDataSet.html")

def clear_database(request):
    return render(request, "clear_database.html")

def delete_item(request):
    if request.method == "POST":
        form = deleteItemForm(request.POST)

        if form.is_valid():
            itemID = form.cleaned_data['ItmID_inv']
            if deleteItem(itemID):
                context = {
                    'form' : form,
                    'error': "Item deleted!"
                }
                return render(request, "delete_item.html", context)
            else:
                context = {
                    'form' : form,
                    'error': "Error Occurred"
                }
                return render(request, "delete_item.html", context)

    else:
        form = deleteItemForm()
        context = {
                    'form' : form,
                    'error': " "
                }
        return render(request, "delete_item.html", context)

def about_us(request):
    return render(request, "about_us.html")
