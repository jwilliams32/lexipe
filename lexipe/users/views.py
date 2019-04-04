from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has now been created! Now you can login!!')

            return redirect('/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# @login_required(login_url="/accounts/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            return redirect('registration/change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
    return render(request, 'registration/change_password.html', args)
