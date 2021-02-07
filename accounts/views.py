from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from decouple import config
import requests

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # First verify captcha challenge
            captcha_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                    'secret': config('RECAPTCHA_PRIVATE_KEY'),
                    'response': request.POST.get('g-recaptcha-response')
                })
            # print(captcha_response.json())
            if captcha_response.json()['success'] == True or captcha_response.json()['error-codes'] == ['timeout-or-duplicate']:
                user = form.save()
                auth_login(request, user)
                return redirect('home')
            return redirect(reverse('signup') + '?captcha=failed')
    else :
        form = SignupForm()
    return render(request, 'signup.html', { 'form': form })

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_context_data(self, **kwargs):
        self.captcha = self.request.GET.get('captcha', None)
        kwargs['captcha'] = self.captcha
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        captcha_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                'secret': config('RECAPTCHA_PRIVATE_KEY'),
                'response': self.request.POST.get('g-recaptcha-response')
            })
        print(captcha_response.json())
        if captcha_response.json()['success'] == True or captcha_response.json()['error-codes'] == ['timeout-or-duplicate']:
            auth_login(self.request, form.get_user())
            return redirect('home')
        return redirect(reverse('login') + '?captcha=failed')

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


