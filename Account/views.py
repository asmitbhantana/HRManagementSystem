from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.views.generic import FormView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserSignupForm

User = get_user_model()


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Account/login.html'
    success_url = reverse_lazy('dashboard:index')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        else:
            form.add_error('username', "Error On Credentials")
        return redirect('dashboard:index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        else:
            return super().get(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('dashboard:index')


class UserSignupView(FormView):
    form_class = UserSignupForm
    template_name = 'Account/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        new_user = User(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'],
                        email=cleaned_data['email'], username=cleaned_data['username'])
        print("User is", new_user)
        new_user.save()
        new_user.set_password(cleaned_data['password1'])
        new_user.save()

        messages.success(self.request, 'Registration Success Please Login')

        return redirect('user:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        else:
            return super().get(request, *args, **kwargs)


class ListUserView(ListView):
    model = User
    template_name = 'Account/list-user.html'

    def get(self, request, *args, **kwargs):
        if request.user.user_position != 'HR':
            return redirect(reverse_lazy('dashboard:index'))

        return super().get(request, *args, **kwargs)


class EditUserView(UpdateView):
    model = User
    template_name = 'Account/edit-user.html'
    form_class = User
