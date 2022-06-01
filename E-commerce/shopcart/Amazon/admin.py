from django.contrib import admin
from .models import category,product
# Register your models here.

class category_admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,category_admin)

class product_admin(admin.ModelAdmin):
    list_display = ['name','image','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(product,product_admin)