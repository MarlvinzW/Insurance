from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.views.generic import FormView

from accounts.forms import PasswordChange, UserUpdateForm
from accounts_admin.decorators import check_for_permission

user = get_user_model()

"""
    ADMIN DASHBOARD VIEW 
"""


class DashBoardView(LoginRequiredMixin, View):
    template_name = 'accounts_admin/dashboard.html'
    title = f"{settings.PLATFORM_NAME} | DashBoard"

    @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    ADMIN PAYMENTS VIEW 
"""


class PaymentsView(LoginRequiredMixin, View):
    template_name = 'accounts_admin/payments.html'
    title = f"{settings.PLATFORM_NAME} | Payments"

    @check_for_permission
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    ADMIN BENEFICIARIES VIEW 
"""


class BeneficiariesView(LoginRequiredMixin, View):
    template_name = 'accounts_admin/beneficiaries.html'
    title = f"{settings.PLATFORM_NAME} | Beneficiaries"

    # @check_for_permission
    def get(self, request, *args, **kwargs):
        beneficiaries = Beneficiary.objects.all()
        return render(request, self.template_name, {'title': self.title, 'beneficiaries':beneficiaries })

    # @check_for_permission
    def post(self, request, *args, **kwargs):
        pass


"""
    ADMIN ACCOUNT VIEW 
"""


class AccountView(LoginRequiredMixin, FormView):
    title = f"{settings.PLATFORM_NAME} | Account"
    template_name = 'accounts_admin/accounts.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    @check_for_permission
    def get(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'user_update_form': user_update_form})

    @check_for_permission
    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated account details')
            return redirect('accounts_admin:dashboard')
        else:
            messages.warning(request, 'Check you details')
            return redirect('accounts_admin:account')


"""
    ADMIN CHANGE PASSWORD VIEW 
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
                return redirect('accounts_admin:change-password')
            else:
                current_user = request.user
                current_user.set_password(new1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                messages.success(request, 'Password Successfully Changed')
                return redirect('accounts_admin:dashboard')
        else:
            messages.warning(request, 'Wrong Old Password, Please Try Again')
            return redirect('accounts_admin:change-password')
