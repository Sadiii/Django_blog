from django.shortcuts import render, redirect
from users.form import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UpdateProfile, UpdateUserForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid()  and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Updated')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)
    context = {'u_form':u_form,
               'p_form': p_form}
    return render(request,'users/profile.html', context)