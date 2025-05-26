from django.contrib import admin
from .models import Department,  Asset, Maintenance, Staff 

admin.site.register(Department)
admin.site.register(Asset)
admin.site.register(Maintenance)
admin.site.register(Staff)
