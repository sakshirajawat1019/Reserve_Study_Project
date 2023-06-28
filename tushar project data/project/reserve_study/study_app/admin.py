from django.contrib import admin
from .models import Years, Common_Expenses, Replacement_Reserves

# Register your models here.
@admin.register(Years)
class Admin_Years(admin.ModelAdmin):
    pass

@admin.register(Common_Expenses)
class Admin_Common_Expenses(admin.ModelAdmin):
    pass

@admin.register(Replacement_Reserves)
class Admin_Replacement_Reserves(admin.ModelAdmin):
    pass

