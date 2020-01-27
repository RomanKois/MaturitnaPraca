from django.contrib import admin
from items.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    prepopulated_fields = {'url': ('name',)}
admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'url',  'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created', 'category', ]
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'url': ('name',)}
admin.site.register(Product, ProductAdmin)

admin.site.site_header = "Chovatelske potreby Admin site"
