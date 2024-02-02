from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from utils.validate import validate_email, authenticate
from utils.otp import generate_otp
from .models import UserLoginCode
from datetime import timedelta
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse

def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if validate_email(email) != True:
            messages.error(request, "Email already in use")
            return redirect('register')
        
        email_message = EmailMessage (
            'Account Created: Succyloglobalfx', # email subject
            f"Welcome to Succyloglobalfx! Your account has been created successfully.\n\nDate: {datetime.datetime.now()}", # email content
            settings.EMAIL_HOST_USER, # email sender
            [email] # recipients
        )
        email_message.fail_silently = True
        email_message.send()
        
        new_user = User.objects.create_user(
            username = f"{firstname}_{lastname}",
            first_name = firstname,
            last_name = lastname,
            password = password,
            email = email
        )
        new_user.save()
        messages.success(request, "Account created! Login now")
        return redirect('login')
    
    context = {
        "status": True
    }

    return render(request, "signup.html", context)

def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
        
    context = {
        "status": True
    }

    return render(request, "login.html", context)

def Logout(request):
    logout(request)
    return redirect('login')

def ForgotPassword(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')

        search_for_user = User.objects.filter(email=email).exists()

        if search_for_user:
            
            user = User.objects.get(email=email) # get user

            # add an expiration time to code used to reset password
            t1 = datetime.datetime.now() #current time
            t2 = timedelta(minutes=10) # time required to reset password
            expiration_time = t1+t2 # final expiration time

            otp = generate_otp()

            new_login_code = UserLoginCode(user=user, code=otp, expiration=expiration_time)
            new_login_code.save()

            reset_password_url = f"{request.get_host()}/{reverse('reset-password', kwargs={'username': user.username, 'code': otp})}"

            email_message = EmailMessage (
                'Reset Your Password', # email subject
                f"Reset your password using the link below:\n{reset_password_url}", # email content
                settings.EMAIL_HOST_USER, # email sender
                [email] # recipients
            )
            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent')
        
        messages.error(request, f"No user exists with email '{email}' ")
        return redirect('forgot-password')
    
    return render(request, 'forgot-password.html')

def PasswordResetSent(request):

    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'reset_sent.html')

def ResetPassword(request, username, code):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        get_user = User.objects.get(username=username)
        
        get_code = None
        try:
            get_code = UserLoginCode.objects.get(user=get_user, code=code)
        except UserLoginCode.DoesNotExist:
            messages.error(request, 'You do not have the right to reset this password.')
            return redirect('reset-password', username=username, code=code)
        
        # getting user inputs from frontend
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # validate passwords
        if len(password) < 5:
            messages.error(request, 'Password cannot be less than 5 characters')
            return redirect('reset-password', username=username, code=code)

        if password != confirm_password:
            messages.error(request, 'Passwords do not match, try again')
            return redirect('reset-password', username=username, code=code)

        #check if code is still valid
        expiration_date = get_code.expiration
        year = expiration_date.split('-')[0]
        month = expiration_date.split('-')[1].strip('0')
        split_to_two = expiration_date.split(' ')[1]
        split_for_date = expiration_date.split(' ')[0]
        day = split_for_date.split('-')[2]
        hour = split_to_two.split(':')[0]
      
        minute = split_to_two.split(':')[1]

        code_expiration_date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        current_time = datetime.datetime.now()

        #if link has expired
        if current_time > code_expiration_date:
            get_code.delete() # delete code after use
            messages.error(request, 'This link has expired. Proceed to the forgot password reset page to get another link.')
            return redirect('reset-password', username=username, code=code)

        #save password is link is still valid
        else:
            #save new password after validation
            get_user.set_password(confirm_password)
            get_user.save()
            get_code.delete() # delete code after use

            # redirect to login page
            messages.success(request, 'Password successfully changed. Login now')
            return redirect('login')
        
    return render(request, "reset-password.html")