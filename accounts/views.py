# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import DetailView
from django.views import View
from models import Account, RecoverAccount
from forms import RegisterForm, LoginForm, EditAccountForm, ChangeEmailForm, ChangePasswordForm, RecoverAccountForm
from django.utils import timezone
from guests.models import Guest
from rooms.models import Room
import uuid

User = get_user_model()


class AccountRegister(View):
    """View para Registrar nova Conta
    """
    model = Account
    form_class = RegisterForm
    template_name = 'accounts/account_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(email, email, password)
            user.first_name = form.cleaned_data.get('name')
            user.last_name = form.cleaned_data.get('surname')
            user.save()
            account = Account()
            account.user = user
            account.whatsapp = form.cleaned_data.get('whatsapp')
            account.save()
            messages.success(request, 'SUCCESS')
            return redirect('accounts:register')
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)


class AccountUpdate(View):
    """View update Account
    """
    form_class = EditAccountForm
    template_name = 'accounts/account_edit.html'

    def get(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        data = {
            'name' : account.user.first_name,
            'surname': account.user.last_name,
            'whatsapp': account.whatsapp
        }
        form = self.form_class(data)
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            account = get_object_or_404(Account, pk=pk)
            user = account.user
            user.first_name = form.cleaned_data.get('name')
            user.last_name = form.cleaned_data.get('surname')
            user.save()
            account.whatsapp = user.first_name = form.cleaned_data.get('whatsapp')
            account.save()
            messages.success(request, 'SUCCESS')
            return redirect('accounts:login')
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)


class AccountEmailChange(View):
    """View change E-Mail
    """
    form_class = ChangeEmailForm
    template_name = 'accounts/account_change_email.html'

    def get(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        form = self.form_class()
        context_data = {'form': form, 'account':account}
        return render(request, self.template_name, context_data)

    def post(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = account.user
            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'SUCCESS')
            return redirect('accounts:login')
        context_data = {'form': form, 'account':account}
        return render(request, self.template_name, context_data)


class AccountPasswordChange(View):
    """View password change
    """
    form_class = ChangePasswordForm
    template_name = 'accounts/account_change_password.html'

    def get(self, request, pk):
        form = self.form_class()
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)

    def post(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = account.user
            user.set_password(form.cleaned_data['password'])

            user.save()
            messages.success(request, 'SUCCESS')
            return redirect('accounts:login')
        context_data = {'form': form}
        return render(request, self.template_name, context_data)


class AccountDashboard(View):
    """Dashboard view
    """
    template_name = 'accounts/account_dashboard.html'

    def get(self, request):
        account = Account.objects.get(user=self.request.user)

        context_data = {'account': account, }
        return render(request, self.template_name, context_data)


class AccountAnnouncements(View):
    """List announcements
    """
    template_name = 'accounts/account_list_announce.html'

    def get(self, request):
        account = Account.objects.get(user=self.request.user)
        guest_list = Guest.objects.filter(account=account)
        count_guests = guest_list.count()
        room_list = Room.objects.filter(account=account)
        context_data = {'account': account, 'guest_list': guest_list, 'count_guests': count_guests, 'room_list': room_list}
        return render(request, self.template_name, context_data)

class LoginView(View):
    """Login View
    """
    form_class = LoginForm
    template_name = 'accounts/account_login.html'

    def get(self, request):
        form = self.form_class()
        context_data = {'form': form, }
        return render(request, self.template_name, context_data)

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'SUCCESS')
            return redirect('accounts:dashboard')
        context_data = {'form': form}
        return render(request, self.template_name, context_data)


def logout_view(request):
    """Logout
    """
    logout(request)
    return redirect('accounts:login')


def generate_uuid(string_length=24):
    """Method usado para gerar chaves únicas
    """
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def send_change_pass_email(recover):
    """Method usado para enviar E-mail com token de recuperação de conta
    """
    html_message = render_to_string('accounts/email_change_pass.html', context={'recover': recover})
    send_mail('FIND ROOMS - Recuperação de Conta', '', settings.EMAIL_FROM, [recover.email], html_message=html_message)


def confirm_recover_password(request, token):
    """View to check the email to recover account, and consume token sent
    """
    recover = get_object_or_404(RecoverAccount, token=token, status='P')
    recover.token_used = timezone.now()
    recover.status = 'C'
    recover.save()
    list_recover = RecoverAccount.objects.filter(email=recover.email)
    if len(list_recover) > 0:
        for rec_item in list_recover:
            rec_item.status = 'E'
            rec_item.save()
    return redirect('accounts:change_password', pk=recover.account.id)


class Recover(View):
    """View to recover account
    """
    form_class = RecoverAccountForm
    template_name = 'accounts/account_recover.html'

    def get(self, request):
        form = self.form_class()
        context_data = {'form': form,}
        return render(request, self.template_name, context_data)

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            account = Account.objects.get(user=user)
            recover = RecoverAccount()
            recover.account = account
            recover.email = email
            recover.token = generate_uuid()
            recover.save()
            send_change_pass_email(recover)
            messages.success(request, 'SUCCESS')
            return redirect('accounts:login')
        context_data = {'form': form}
        return render(request, self.template_name, context_data)


def index_view(request):
    """Index view
    """
    return render(request, 'index.html')
