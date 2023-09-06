from django.contrib import admin
from .models import Element

class ElementTable(admin.ModelAdmin):
    """Representation of the Elements table."""
    list_display = (
        'id',
        'atomic_number',
        'atomic_mass',
        'symbol',
        'group',
    )
    list_per_page = 25
    ordering = ['atomic_number', 'id']

    def get_atomic_mass(self, obj):
        return obj.atomic_mass
    

admin.site.register(Element, ElementTable)
# Register your models here.
