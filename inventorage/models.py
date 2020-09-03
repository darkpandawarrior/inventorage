from django.db import models
from django.utils.timezone import now

# Create your models here.
class items_inv(models.Model):
    itemsID_inv = models.CharField(primary_key = True, max_length=50, verbose_name = 'Item ID')
    itemsDesc_inv = models.CharField(max_length=200, verbose_name = 'Description')
    itemsQnt_inv = models.IntegerField(verbose_name = 'Quantity')
    itemsCostPrice_inv = models.IntegerField(verbose_name = 'Cost Price')
    itemsSellPrice_inv = models.IntegerField(verbose_name = 'Selling Price')
    itemsTotalPrice_inv = models.IntegerField(verbose_name = 'Total Price')

    def __str__(self):
       return self.itemsID_inv

class transactions_inv(models.Model):
    OrderID_inv = models.AutoField(primary_key = True, verbose_name = 'Order ID')
    ItmID_inv = models.ForeignKey(items_inv, on_delete= models.DO_NOTHING, verbose_name = 'Item ID')
    Discount_inv = models.FloatField(verbose_name = 'Discount (%)')
    Amount_inv = models.FloatField(verbose_name = 'Amount')
    Date_inv = models.DateTimeField(default=now, verbose_name = 'Date and Time')
    ImtQnt_inv = models.IntegerField(verbose_name = 'Quantity')
    class Meta:
        unique_together = (('OrderID_inv','ItmID_inv'),)
    def __str__(self):
        return self.OrderID_inv