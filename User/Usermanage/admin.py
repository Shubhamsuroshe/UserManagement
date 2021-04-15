from django.contrib import admin
from Usermanage.models import UserProfile, Roles

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Roles)