from django.contrib import admin
from .models import SheetMaterial, LineMaterial, Lock, Furniture, Hinge, Handle

admin.site.register(SheetMaterial)
admin.site.register(LineMaterial)
admin.site.register(Lock)
admin.site.register(Furniture)
admin.site.register(Hinge)
admin.site.register(Handle)
