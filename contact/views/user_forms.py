from django.shortcuts import redirect, render
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('contact:user_update')    
    

    return render(
        request,
        'contact/user_update.html',
        {
            'form': form,
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('contact:login')
        messages.error(request, 'Invalid username/password.')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')