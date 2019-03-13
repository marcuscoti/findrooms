from models import Account
from django.shortcuts import get_object_or_404

def get_account_by_user(user):
    return get_object_or_404(Account, user=user)