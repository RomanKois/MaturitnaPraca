from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    url = models.SlugField(db_index=True, unique= True, blank=True, null=True)
  

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('item:category', args=[str(self.url)])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    url = models.SlugField(db_index=True, unique= True, blank=True, null=True)
    image = models.ImageField(upload_to='products/products', blank=True)
    descripton = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
 

    class Meta:
        ordering = ('-created',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        index_together = (('id', 'url'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item:product_detail', args=[self.id, self.url])