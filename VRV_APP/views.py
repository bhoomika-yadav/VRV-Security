from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.utils import timezone
from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

from django.http import HttpResponse
from .models import userdetails
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from .forms import CreateUserForm
from datetime import datetime
def validate_phone(phone):
    """Validates a phone number to ensure it's 10 digits and starts with specific ranges."""
    pattern = r'^[6-9]\d{9}$'  # Starts with 6, 7, 8, or 9 and has 10 digits
    return re.match(pattern, phone)
def RegisterView(request):
    if request.method == 'POST':
        errors = {}
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('number', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        dob = request.POST.get('dob', '').strip()
        user_type = request.POST.get('user_type', '').strip()
        # Validate each field
        user_objects = User.objects.filter(username=username)
        user_objects1 = User.objects.filter(email=email)
        messages.error(request, "Passwords do not match!")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if not phone:
                errors['number'] = "Phone number is required."
            elif not validate_phone(phone):
                errors['number'] = "Invalid phone number. It should be 10 digits and start with 6-9."
            elif userdetails.objects.filter(phone=phone).exists():
                errors['number'] = "Phone number already exists."
            if not dob:
                errors['dob'] = "Date of birth is required."

            if not user_type:
                errors['user_type'] = "User type is required."
            if errors:
                return render(request, "register.html", {
                    'errors': errors,
                    'name': username,
                    'email': email,
                    'number': phone,
                    'dob': dob,
                    'user_type': user_type,
                    "form":form
                })
            new_user = form.save()
            userdetails.objects.create(
            client_id=new_user.id, 
            phone=phone, 
            dob=dob, 
            user_type=user_type
            )
            return redirect('login')
        else:
            return render(request, "register.html", {"form": form})
    form=CreateUserForm()
    return render(request, "register.html",{"form":form})

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from VRV_APP.models import userdetails
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# import requests

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta
import jwt
import secrets

# JWT Secret and Algorithm
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'email': user.client.email,
        'exp': datetime.utcnow() + timedelta(hours=1),  # Token expiration
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


# Function to generate tokens for all users
def generate_tokens_for_all_users(request,id):
    user = userdetails.objects.get(id=id)
    user_tokens = []
    token = generate_jwt_token(user)
    user.user_token=token
    user.status='ACTIVE'
    user.token_creation_time= timezone.now()
    user.save()
    return redirect('user_details')

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import userdetails
def LoginView(request):
    if request.method == 'POST':
        user_email = request.POST.get('username')  # Assuming 'username' holds the email
        user_password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=user_email, password=user_password)

        if user:
            user_details = userdetails.objects.filter(client_id=user.id).first()

            if user.is_superuser:
                login(request, user)
                return render(request, 'dashboard.html')
            elif user_details:
                if user_details.user_type == 'Client' and user_details.status=="ACTIVE":
                    login(request, user)
                    return redirect('client_dashboard')  # Replace with actual URL name
                elif user_details.user_type == 'Moderator' and user_details.status=="ACTIVE":
                    login(request, user)
                    return redirect('moderator_dashboard')
                else:
                    messages.error(request, "Unauthorized user type!")
            else:
                messages.error(request, "User details not found!")
        else:
            messages.error(request, "Invalid email or password!")
    
    return render(request, "login.html")



def LogoutView(request):
    return redirect('login')

def user_details(request):
    user_detail = userdetails.objects.all()
    present_time=timezone.now()
    threshold = timedelta(minutes=30)
    for i in user_detail:
        if i.token_creation_time:
            if present_time-i.token_creation_time>threshold:
                i.status='DEACTIVE'
                i.save()
    user_detail = userdetails.objects.all()
    return render(request, "user_details.html", {"user_details": user_detail})


def client_dashboard(request):
    return render(request,'client_dashboard.html')

def moderator_dashboard(request):
    return render(request, 'moderator_dashboard.html')
