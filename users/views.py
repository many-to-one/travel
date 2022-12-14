from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, \
    DeleteView, ListView
from django.contrib import messages
from posts.models import Post
from .models import *
from .forms import BlogUserCreationForm, BlogUserChangeForm, BlogPhotoChangeForm
from django.urls import reverse_lazy


def success(request):
    return render(request, 'success.html')


class CreateUser(CreateView):
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create_user.html'


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            messages.success(request, f'Hello, {user}')
            return redirect('home')
        else:
            messages.error(request, 'Your username or password is incorrect')
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Log out')
    return redirect('login')


class UpdateUser(UpdateView):
    model = BlogUser
    form_class = BlogUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update_user.html'


class ProfileView(DetailView):
    model = BlogUser
    context_object_name = 'user'
    queryset = BlogUser.objects.all()
    template_name = 'profile_view.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['posts'] = Post.objects.filter(author_id=self.kwargs['pk'])
        return context


class DeleteUser(DeleteView):
    model = BlogUser
    success_url = reverse_lazy('home')
    template_name = 'delete_profile.html'
