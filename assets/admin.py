from django.contrib import admin
from .models import Department, Asset, Maintenance

admin.site.register(Department)
admin.site.register(Asset)
admin.site.register(Maintenance)
