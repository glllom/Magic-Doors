from django.contrib import admin
from .models import ProductClass, ProductFamily, Product, PresetGroup, Preset, Engraving, Window, LockPocket, HingePocket, ExtraPocket

admin.site.register(ProductClass)
admin.site.register(ProductFamily)
admin.site.register(Product)
admin.site.register(PresetGroup)
admin.site.register(Preset)
admin.site.register(Engraving)
admin.site.register(Window)
admin.site.register(LockPocket)
admin.site.register(HingePocket)
admin.site.register(ExtraPocket)
