from django.contrib import admin

from . import models

# Register your models here.

class ClosedLoanAdmin(admin.ModelAdmin):
    list_display = ['loan_number', 'purpose', 'borrower' ]

admin.site.register(models.ClosedLoan, ClosedLoanAdmin)
