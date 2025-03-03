
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
User = get_user_model()

import string
from django.utils.crypto import get_random_string

class CustomAuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        try:

            user = User.objects.get(Q(email=username))
            if password != None:
                pwd_valid = user.check_password(password)
                if pwd_valid:
                    return user
            return None
        except Exception as e:
            raise e