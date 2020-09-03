from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django import forms

item = items_inv.object.get(itemsID_inv = "A000015")