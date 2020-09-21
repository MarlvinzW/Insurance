from django.urls import path
from .views import DashBoardView, PaymentsView, BeneficiariesView, AccountView, ChangePasswordView,delete_payment

urlpatterns = [
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('payments/', PaymentsView.as_view(), name='payments'),
    path('beneficiaries/', BeneficiariesView.as_view(), name='beneficiaries'),
    path('accounts/', AccountView.as_view(), name='accounts'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('delete/payment/<payment_id>/', delete_payment, name='delete_payment'),

]
