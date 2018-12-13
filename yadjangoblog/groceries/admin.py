from django.contrib import admin
from groceries.models import CompanyCategory, Company

# Register your models here.
@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass