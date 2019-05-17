from django.contrib import admin
from .models import Roles, BranchsRoles, CBranchs

# Register your models here.
admin.site.register(Roles)
admin.site.register(CBranchs)
admin.site.register(BranchsRoles)