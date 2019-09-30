from django.contrib import admin
from firstapp.models import UserRole,SiteUser
# Register your models here.
admin.site.register(UserRole)
admin.site.register(SiteUser)
