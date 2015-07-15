from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Item, ItemAdmin)
