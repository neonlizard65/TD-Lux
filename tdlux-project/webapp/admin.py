from django.contrib import admin
from . import models

admin.site.register(models.Client)
admin.site.register(models.Product)
admin.site.register(models.Sklad)
admin.site.register(models.Employee)
admin.site.register(models.Zayavka)
