import csv

from loans.models import ClosedLoan, NeedsDisclosed

def init_closed():
     with open('./mock/closed_loans.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = ClosedLoan.objects.get_or_create(
                    loan_officer = row[0],
                    loan_number = row[1],
                    borrower = row[2],
                    total_loan_amount = row[3],
                    current_milestone = row[4],
                    loan_type = row[5],
                    purpose = row[6],
                    est_funding_date =row[7],
                    loan_status = row[10]
                )

def init_needs_disclosed():
     with open('./mock/needs_disclosed.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = NeedsDisclosed.objects.get_or_create(
                    loan_officer = row[1],
                    loan_number = row[0],
                    borrower = row[2],
                    sub_prop_street = row[4],
                    sub_prop_city = row[5],
                    sub_prop_state = row[6],
                    sub_prop_zip = row[7],
                    sub_prop_est_value = row[8],
                    loan_amount = row[9],
                    application_date = row[10],
                    disclosures_due_date = row[11]
                )
