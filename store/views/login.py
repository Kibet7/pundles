# views/login.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from store.models.user import CustomUser  # Ensure you import your custom user model

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        phone_number = request.POST.get('phone')  # Safely get the phone number
        password = request.POST.get('password')  # Safely get the password
        
        if not phone_number or not password:
            messages.error(request, 'Please enter both phone number and password.')
            return render(request, 'store/login.html')
        
        try:
            # Find user by phone number
            user_instance = CustomUser.objects.get(phone_number=phone_number)
            
            # Authenticate using the username and password
            user = authenticate(request, username=user_instance.username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('store:lucky_box')  # Redirect to lucky box game after login
            else:
                messages.error(request, 'Invalid phone number or password.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User with this phone number does not exist.')

    return render(request, 'store/login.html')

def logout_view(request):
    """Log out the user and redirect to the login page."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('store:login')  # Adjust to your login URL name
