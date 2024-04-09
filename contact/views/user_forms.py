from email import message
from django.shortcuts import redirect, render
from contact.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            redirect('user/register')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )