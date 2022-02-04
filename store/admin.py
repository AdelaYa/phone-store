from django.contrib import admin
from .models import Manufacturer, Phone, Review


admin.site.register(Manufacturer)
admin.site.register(Review)


class ReviewInLine(admin.StackedInline):
    model = Review


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('model', 'proc', 'ram', 'rom', 'color', 'count', 'price')
    prepopulated_fields = {'slug': ('model', 'color', 'ram')}
    search_fields = ('model', 'proc', 'ram', 'rom', 'color')
    date_hierarchy = 'created'
    ordering = ('created', )
    inlines = [
        ReviewInLine,
    ]

