from .models import *
from .forms import *
from .views import *
from django.core.exceptions import ObjectDoesNotExist

def createTransaction( id, discount, date, quantity):
    try:
        item = items_inv.objects.get(itemsID_inv = id)
        if item.itemsQnt_inv >= quantity:
            amount = quantity * item.itemsSellPrice_inv*(100.0 - discount)/100
            item.itemsQnt_inv = item.itemsQnt_inv - quantity
            item.itemsTotalPrice_inv = item.itemsTotalPrice_inv - quantity*item.itemsCostPrice_inv
            item.save()
            transactions_inv.objects.create(ItmID_inv = id , Discount_inv = discount, Amount_inv = amount, Date_inv = date, ImtQnt_inv= quantity)
            return True
        else :
            return False
    except ObjectDoesNotExist:
        return False

def createItem(itemID, description, quantity, CP, SP):
    total = CP * quantity
    item = items_inv.objects.create(itemsID_inv  = itemID, itemsDesc_inv = description, itemsQnt_inv = quantity, itemsCostPrice_inv = CP,
                itemsSellPrice_inv = SP, itemsTotalPrice_inv = total)
    if item:
        return True
    else:
        return False
def updateItem(itemID, quantity, CP, SP):
    try:
        item = items_inv.objects.get(itemsID_inv = itemID)
        item.itemsQnt_inv = item.itemsQnt_inv + quantity
        if CP:
            item.itemsCostPrice_inv = CP
        if SP:
            item.itemsSellPrice_inv = SP
        total = item.itemsQnt_inv * item.itemsCostPrice_inv
        item.itemsTotalPrice_inv = total
        item.save()
        return True
    except ObjectDoesNotExist:
        return False
def getItemTable():
    return items_inv.objects.all()

def getTransactionsTable():
    queryset =  transactions_inv.objects.all()
    return queryset.reverse()

def lowQItem():
    queryset = items_inv.objects.filter(itemsQnt_inv__lte = 3)
    return queryset

def deleteItem(itemID):
    return items_inv.objects.get(itemsID_inv = itemID).delete()