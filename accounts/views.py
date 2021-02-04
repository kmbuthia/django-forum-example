from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from accounts.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Account creation disabled. Show popup then redirect back to home page.
            # To create accounts for others, you could enable the admin area and create
            # them from there.
            # return redirect(reverse('home') + '?signup=disabled')
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else :
        form = SignupForm()
    return render(request, 'signup.html', { 'form': form })

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


