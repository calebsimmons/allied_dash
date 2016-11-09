from django.contrib import admin

from . import models

# Register your models here.

class ClosedLoanAdmin(admin.ModelAdmin):
    list_display = ['loan_number', 'purpose', 'borrower' ]

class NeedsDisclosedAdmin(admin.ModelAdmin):
    list_display = ['loan_number', 'borrower', 'disclosures_due_date']

admin.site.register(models.ClosedLoan, ClosedLoanAdmin)
admin.site.register(models.NeedsDisclosed, NeedsDisclosedAdmin)
