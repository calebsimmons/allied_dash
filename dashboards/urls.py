from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^closed_loans$',views.ClosedLoansDashView.as_view(),
        name='closed_loans'),
]
