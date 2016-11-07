from django.shortcuts import render
from django.views.generic import TemplateView

import arrow

class ClosedLoansDashView(TemplateView):
    template_name = 'dashboards/closed_loans.html'

    def get_context_data(self, **kwargs):
        context = super(ClosedLoansDashView, self).get_context_data(**kwargs)
        context['thirty_days_closed'] = self.thirty_days_closed()
        return context

    def thirty_days_closed(self):
        pass    
