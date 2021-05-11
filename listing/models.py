from django.db import models

# Create your models here.

class Product(models.Model):
    ProductNo = models.IntegerField(verbose_name='کد کالا')
    ProductTitle = models.CharField(max_length=250, verbose_name='عنوان کالا')
    def __str__(self):
       return self.ProductTitle 

    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'