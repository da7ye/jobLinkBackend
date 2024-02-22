from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from base.forms import ProviderForm
from .models import Category, Provider


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile', pk=request.user.id)


    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', pk=user.id)
        else:
            messages.error(request, 'User or passwoed does not exist')

    context = {'page': page}
    return render(request, 'auth/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    user_form = UserCreationForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('provider/providerForm')

        else:
            messages.error(request, 'An error occurred while registering')

    context = {'user_form': user_form}
    return render(request, 'auth/login_register.html', context)


@login_required(login_url='login')
def providerForm(request):
    user = request.user
    categories = Category.objects.all()

    if request.method == 'POST':
        provider_form = ProviderForm(request.POST)

        if provider_form.is_valid():
            provider = provider_form.save(commit=False)
            provider.user = user
            provider.save()
            messages.success(request, 'Profile creation successful')
            return redirect('profile', pk=user.id)
        else:
            messages.error(request, 'An error occurred while creating the profile')

    else:
        provider_form = ProviderForm()

    context = {'provider_form': provider_form, 'categories': categories}
    return render(request, 'provider/providerForm.html', context)

        
def registerPage(request):
    user_form = UserCreationForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid() :
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('providerForm')
        else:
            messages.error(request, 'An error occurred while registering')

    context = {'user_form': user_form}
    return render(request, 'auth/login_register.html', context)



def home(request):
    q =  request.GET.get('q') if request.GET.get('q') != None else ''

    catagories = Category.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q)
    )

    Category_count = catagories.count()
    context = {'catagories' : catagories, 'Category_count' : Category_count}
    return render(request, 'main/home.html',  context)


def catagoryProviders(request, pk):
    category = Category.objects.get(id=pk)
    # provider = Provider.objects.get(id=pk)
    # user_id = provider.user.id
    context = {'catagories': [category]}
    return render(request, 'main/catagoryProviders.html', context)


def profile(request, pk):
    provider = Provider.objects.get(user=pk)
    context = {'provider' : provider}
    return render(request, 'provider/profile.html', context)
