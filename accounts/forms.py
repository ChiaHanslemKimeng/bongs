from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import ResetPasswordForm

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full bg-brand-muted border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-brand-accent focus:ring-1 focus:ring-brand-accent'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full bg-brand-muted border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-brand-accent focus:ring-1 focus:ring-brand-accent'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full bg-brand-muted border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-brand-accent focus:ring-1 focus:ring-brand-accent'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-brand-muted border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-brand-accent focus:ring-1 focus:ring-brand-accent'}),
        }

class CustomResetPasswordForm(ResetPasswordForm):
    def clean_email(self):
        email = super().clean_email()
        if not User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email address is not associated with any account.")
        return email
