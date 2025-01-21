from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'store/password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'store/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'store/password_reset_confirm.html'

password_reset_view = CustomPasswordResetView.as_view()
password_reset_done_view = CustomPasswordResetDoneView.as_view()
password_reset_confirm_view = CustomPasswordResetConfirmView.as_view()
