from django.db import models


# Create your models here.
class ClosedLoan(models.Model):
    loan_officer = models.CharField(max_length=255)
    loan_number = models.IntegerField(unique=True, primary_key=True)
    borrower = models.CharField(max_length=255)
    total_loan_amount = models.IntegerField(null=True)
    current_milestone = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    est_funding_date = models.DateField(null=True)
    funds_sent_date = models.DateField(null=True)
    funded_milestone_date = models.DateField(null=True)
    loan_status = models.CharField(max_length=255)


class NeedsDisclosed(models.Model):
    loan_number = models.IntegerField(unique=True, primary_key=True)
    loan_officer = models.CharField(max_length=255)
    borrower = models.CharField(max_length=255)
    sub_prop_street = models.CharField(max_length=255)
    sub_prop_city = models.CharField(max_length=255)
    sub_prop_state = models.CharField(max_length=255)
    sub_prop_zip = models.CharField(max_length=255)
    sub_prop_est_value = models.CharField(max_length=255)
    loan_amount = models.IntegerField()
    application_date = models.DateField()
    disclosures_due_date = models.DateField()
