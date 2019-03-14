# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
User = get_user_model()


class RegisterForm(forms.Form):

    email = forms.EmailField(label='E-mail')
    email2 = forms.EmailField(label='Confirme o E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)
    name = forms.CharField(label='Nome')
    surname = forms.CharField(label='Sobrenome')
    whatsapp = forms.CharField(label='WhatsApp')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        whatsapp = self.cleaned_data.get('whatsapp')

        if email != email2:
            #raise forms.ValidationError('Os emails não são iguais!')
            self.add_error('email', 'Os emails não são iguais!')
        emails_qs = User.objects.filter(email=email)
        if emails_qs.exists():
            self.add_error('email', 'Email já cadastrado! Use outro.')
        if password != password2:
            self.add_error('password', 'As senhas não são iguais!')
        if len(whatsapp) == 0:
            self.add_error('whatsapp', 'Você deve informar um WhatsApp.')
        return super(RegisterForm, self).clean(*args, **kwargs)


class EditAccountForm(forms.Form):

    name = forms.CharField(label='Nome')
    surname = forms.CharField(label='Sobrenome')
    whatsapp = forms.CharField(label='WhatsApp')


class ChangeEmailForm(forms.Form):

    email = forms.EmailField(label='Novo E-mail')
    email2 = forms.EmailField(label='Confirme o E-mail')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            self.add_error('email', 'Os emails não são iguais!')
        else:
            emails_qs = User.objects.filter(email=email)
            if emails_qs.exists():
                self.add_error('email', 'Este email já existe, use outro!')
        return super(ChangeEmailForm, self).clean(*args, **kwargs)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            self.add_error('password', 'As senhas não são iguais!')
        return super(ChangePasswordForm, self).clean(*args, **kwargs)


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        emails_qs = User.objects.filter(email=email)
        if emails_qs.exists():
            user = authenticate(username=email, password=password)
            if user is None:
                self.add_error('password', 'Senha incorreta!')
            else:
                if not user.is_active:
                    self.add_error('email', 'Usuário não ativo!')
        else:
            self.add_error('email', 'Email não cadastrado!')
        return super(LoginForm, self).clean(*args, **kwargs)


class RecoverAccountForm(forms.Form):

    email = forms.EmailField(label='Seu E-mail')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        emails_qs = User.objects.filter(email=email)
        if not emails_qs.exists():
            self.add_error('email', 'Não existe conta cadastrada com esse e-mail')
        return super(RecoverAccountForm, self).clean(*args, **kwargs)