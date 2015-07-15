# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_initial(apps, schema_editor):
    Size = apps.get_model('main', 'Size')
    sizes = {}
    for size in ['XS', 'S', 'M', 'L', 'XL']:
        sizes[size] = Size.objects.create(name=size)

    Item = apps.get_model('main', 'Item')
    item1 = Item.objects.create(name='The Itcher', description='Scratch any itch', cost=27.0)
    item1.sizes.add(sizes['XL'])
    item2 = Item.objects.create(name='The Blinger', description='Diamonds', cost=343.0)
    item2.sizes.add(sizes['L'])
    item3 = Item.objects.create(name='Glitz and Gold', description='Gold handle and fancy emeralds make this shine',
                                cost=4343.0)
    item3.sizes.add(*[sizes[key] for key, size in sizes.items() if key != 'XS'])


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial),
    ]
