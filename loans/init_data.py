import csv

from loans.models import ClosedLoan

def init_closed():
     with open('./mock/closed_loans.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = ClosedLoan.objects.get_or_create(
                    loan_officer = row[0],
                    loan_number = row[1],
                    borrower = row[2],
                    total_loan_ammount = row[3],
                    current_milestone = row[4],
                    loan_type = row[5],
                    purpose = row[6],
                    est_funding_date =row[7],
                    loan_status = row[10]
                )
