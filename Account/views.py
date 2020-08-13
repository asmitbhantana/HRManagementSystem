from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserSignupForm


User = get_user_model()


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Accounts/login.html'
    success_url = reverse_lazy('blog:index')

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        print(context)
        return context

    def form_valid(self, form):
        user = authenticate(email=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        else:
            form.add_error('email', "Error On Credentials")
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('blog:index')


class UserSignupView(FormView):
    form_class = UserSignupForm
    template_name = 'Account/register.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        # profile_image = request.FILES['profile_image']
        # if profile_image.name.endswith(".jpeg") or profile_image.name.endswith(
        #         '.jpg') or profile_image.name.endswith(".png"):
        #     fs = FileSystemStorage()
        #     filename = fs.save(profile_image.name, profile_image)
        # print("File name is", filename)
        new_user = User(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'],
                        email=cleaned_data['email'], username=cleaned_data['username'], is_active=False)
        print("User is", new_user)
        new_user.save()
        new_user.set_password(cleaned_data['password1'])
        new_user.save()

        messages.success(self.request, 'Registration Success Please Login')

        return redirect('account:login')


