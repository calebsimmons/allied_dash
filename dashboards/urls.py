from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^closed_loans$', views.ClosedLoansDashView.as_view(),
        name='closed_loans'),
    url(r'^needs_disclosed$', views.NeedsDisclosedDashView.as_view(),
        name='needs_disclosed')    
]
