from django.db import models


# Create your models here.
class ClosedLoan(models.Model):
    loan_officer = models.CharField(max_length=255)
    loan_number = models.IntegerField(unique=True, primary_key=True)
    borrower = models.CharField(max_length=255)
    total_loan_ammount = models.IntegerField(null=True)
    current_milestone = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    est_funding_date = models.DateField(null=True)
    funds_sent_date = models.DateField(null=True)
    funded_milestone_date = models.DateField(null=True)
    loan_status = models.CharField(max_length=255)
