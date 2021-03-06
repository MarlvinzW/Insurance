from django.urls import path
from .views import DashBoardView, PaymentsView, BeneficiariesView, AccountView, ChangePasswordView,delete_payment, \
edit_payment, edit_beneficiary, delete_beneficiary, create_beneficiary, make_payment

urlpatterns = [
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('payments/', PaymentsView.as_view(), name='payments'),
    path('beneficiaries/', BeneficiariesView.as_view(), name='beneficiaries'),
    path('create_beneficiary/', create_beneficiary, name='create_beneficiary'),
    path('accounts/', AccountView.as_view(), name='accounts'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('make-payment/', make_payment, name='make_payment'),
    path('delete/payment/<payment_id>/', delete_payment, name='delete_payment'),
    path('edit/payment/<payment_id>/', edit_payment, name='edit_payment'),
    path('delete/beneficiary/<beneficiary_id>/', delete_beneficiary, name='delete_beneficiary'),
    path('edit/beneficiary/<beneficiary_id>/', edit_beneficiary, name='edit_beneficiary'),


]
