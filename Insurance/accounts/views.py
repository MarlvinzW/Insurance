from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.views.generic import FormView
from django.http import HttpResponseRedirect

from accounts.decorators import check_for_permission
from accounts.forms import UserUpdateForm, PasswordChange
from payments.models import *

user = get_user_model()

"""
    DASHBOARD VIEW 
"""


class DashBoardView(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    title = f"{settings.PLATFORM_NAME} | DashBoard"

    @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    PAYMENTS VIEW 
"""


class PaymentsView(LoginRequiredMixin, View):
    template_name = 'accounts/payments.html'
    title = f"{settings.PLATFORM_NAME} | Payments"

    model = Payment

    # @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    def get_queryset(self, *args, **kwargs): 
        qs = super(Payment, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
        return qs 

    # @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    BENEFICIARIES VIEW 
"""


class BeneficiariesView(LoginRequiredMixin, View):
    template_name = 'accounts/beneficiaries.html'
    title = f"{settings.PLATFORM_NAME} | Beneficiaries"

    @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    ACCOUNT VIEW 
"""


class AccountView(LoginRequiredMixin, FormView):
    title = f"{settings.PLATFORM_NAME} | Account"
    template_name = 'accounts/accounts.html'

    # @check_for_permission
    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    # @check_for_permission
    def get(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'user_update_form': user_update_form})

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated account details')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Check you details')
            return redirect('account')


"""
    CHANGE PASSWORD VIEW 
"""


class ChangePasswordView(LoginRequiredMixin, FormView):
    title = f"{settings.PLATFORM_NAME} | Change Password"
    template_name = 'accounts/change-password.html'
    form_class = PasswordChange

    def get_context_data(self, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(request.user)})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        old = request.POST.get('old_password')
        new1 = request.POST.get('new_password1')
        new2 = request.POST.get('new_password2')
        if authenticate(request, username=request.user.username, password=old):
            if new1 != new2:
                messages.warning(request, "Passwords Don't Match")
                return redirect('change-password')
            else:
                current_user = request.user
                current_user.set_password(new1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                messages.success(request, 'Password Successfully Changed')
                return redirect('dashboard')
        else:
            messages.warning(request, 'Wrong Old Password, Please Try Again')
            return redirect('change-password')


def delete_payment(request, payment_id):
    payment = Payment.objects.filter(id=payment_id).first() 

    context = {
        'payment': payment
    }

    if request.method == "POST":
        payment = Payment.objects.filter(id=int(request.POST['payment_id'])).first()
        payment.delete()
        messages.success(request, 'Successfully Deleted Payment')
        return redirect('accounts')
        
        

    return render(request, 'accounts/payment_delete.html', context=context)

def edit_payment(request, payment_id):
    payment = Payment.objects.filter(id=payment_id).first() 

    context = {
        'payment': payment
    }

    if request.method == "POST":
        is_paid = False
        payment = Payment.objects.filter(id=int(request.POST['payment_id']))

        if request.POST['has_paid'] == 'on': is_paid = True

        payment.update(
            email = request.POST['email'],
            reference=request.POST['reference'],
            amount = request.POST['amount'],
            status_url = request.POST['status_url'],
            payment_url = request.POST['payment_url'],
            has_paid = is_paid
        )


        
        messages.success(request, 'Successfully Updated Payment')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 

        
        

    return render(request, 'accounts/payment_edit.html', context=context)    
