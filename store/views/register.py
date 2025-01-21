# views/register.py
from django.shortcuts import render, redirect
from store.models.user import CustomUser   # Import the custom user model
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        phone_number = request.POST['phone_number']

        if password == password_confirm:
            try:
                user = CustomUser .objects.create_user(username=username, password=password, phone_number=phone_number)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('store:login')  # Change as needed
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'store/register.html')