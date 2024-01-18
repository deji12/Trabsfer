from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def validate_email(email):

    if not User.objects.filter(email=email).exists():
        return True
    else:
        return False
    
def authenticate(email, password):
    UserModel = get_user_model()
    
    try:
        get_user = UserModel.objects.get(email=email)
        if get_user.check_password(password):
            return get_user
        else:
            return None

    except User.DoesNotExist:
        return None