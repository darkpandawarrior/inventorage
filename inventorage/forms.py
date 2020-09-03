from django import forms
from django.db import models
from .models import items_inv, transactions_inv

class addItemForm (forms.ModelForm):
    class Meta:
        model = items_inv
        fields = ('itemsID_inv','itemsDesc_inv','itemsQnt_inv','itemsCostPrice_inv','itemsSellPrice_inv')

class updateInv(forms.ModelForm):
    class Meta:
        model = transactions_inv
        fields = ('ItmID_inv',)
    quantity = forms.IntegerField()
    Cost_price = forms.IntegerField(required = False)
    Selling_price = forms.IntegerField(required = False)


class addTransaction(forms.ModelForm):
    class Meta:
        model = transactions_inv
        fields = ('ItmID_inv','Discount_inv','Date_inv','ImtQnt_inv')

class deleteItemForm(forms.ModelForm):
    class Meta:
        model = transactions_inv
        fields = ('ItmID_inv',)