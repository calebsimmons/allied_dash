import collections

from datetime import date, timedelta, time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from loans.models import ClosedLoan, NeedsDisclosed
from .utils import month_delta


class ClosedLoansDashView(ListView):
    context_object_name = 'closed_loans'
    template_name = 'dashboards/closed_loans.html'
    fields = ('loan_number','funds_sent_date')
    model = ClosedLoan

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = ClosedLoan.objects.all()
        context = super(ClosedLoansDashView, self).get_context_data(**kwargs)
        context['thirty_days_closed'] = self.thirty_days_closed()
        context['thirty_days_closed_cml'] = self.thirty_days_closed_cml()
        return context

    def thirty_days_closed(self):
        final_data = collections.OrderedDict()
        day = date.today() + timedelta(-30)
        for i in range(1,30):
            day = day + timedelta(1)
            count = ClosedLoan.objects.filter(
                    est_funding_date__year=str(day.year)
                ).filter(
                    est_funding_date__month=str(day.month)
                ).filter(
                    est_funding_date__day=str(day.day)
                ).count()


            final_data[str(day)] = count

        return {
            'day_labels': list(final_data.keys()),
            'counts': list(final_data.values())
        }

    def thirty_days_closed_cml(self):
        final_data = collections.OrderedDict()
        day = date.today() + timedelta(-30)
        sum = 0
        for i in range(1,30):
            day = day + timedelta(-1)
            count = ClosedLoan.objects.filter(
                    est_funding_date__year=str(day.year)
                ).filter(
                    est_funding_date__month=str(day.month)
                ).filter(
                    est_funding_date__day=str(day.day)
                ).count()

            sum += count
            final_data[str(day)] = sum

        return {
            'day_labels': list(final_data.keys()),
            'sums': list(final_data.values())
        }

class NeedsDisclosedDashView(ListView):
    context_object_name = 'needs_disclosed'
    template_name = 'dashboards/needs_disclosed.html'
    fields = ('loan_number', 'loan_officer', 'borrower', 'sub_prop_street',
              'sub_prop_state', 'sub_prop_zip', 'sub_prop_est_value',
              'loan_amount', 'application_date', 'disclosures_due_date')
    model = NeedsDisclosed

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = NeedsDisclosed.objects.all().order_by('disclosures_due_date')
        context = super(NeedsDisclosedDashView, self).get_context_data(**kwargs)
        return context
