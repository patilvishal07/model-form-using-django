from django.contrib import admin
from app.models import vishal

# Register your models here.
class vp(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'price',
        'stock',
        'desc'

    ]

admin.site.register(vishal,vp)
