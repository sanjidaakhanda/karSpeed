from django.contrib import admin
from .models import Brand  

# Register your models here.
# admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('b_name',)}
    list_display = ['b_name','slug']
admin.site.register(Brand,BrandAdmin)

