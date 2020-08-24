from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LoginView, RegistrationView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='pages/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='pages/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html'),
         name='password_reset_complete'),
]
