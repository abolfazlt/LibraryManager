from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .forms import *
from .models import EFile


def index(request):
    if not request.user.is_authenticated:
        return redirect('EFiles:login_user')
    efiles = EFile.objects.all()
    return render(request, 'EFiles/index.html',
                  {'user': request.user, 'efiles': efiles})

def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                efiles = EFile.objects.all()
                return render(request, 'EFiles/index.html',
                              {'user': user, 'efiles': efiles})

    return render(request, 'EFiles/registration_form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('EFiles:login_user')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                efiles = EFile.objects.all()
                return render(request, 'EFiles/index.html',
                              {'user': user, 'efiles': efiles})
            else:
                return render(request, 'EFiles/login_form.html', {'error_message': 'Your account has been disabled'})
    return render(request, 'EFiles/login_form.html')

def detail(request, efile_id):
    if not request.user.is_authenticated:
        return render(request, 'EFiles/login_form.html')
    else:
        user = request.user
        efile = get_object_or_404(EFile, pk=efile_id)
        return render(request, 'EFiles/detail.html', {'efile': efile, 'user': user})

def add_efile(request):
    if not request.user.is_authenticated:
        return redirect('EFiles:login_user')
    else:
        form = EFileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            efile = form.save(commit=False)
            efile.file_content = request.FILES['file_content']
            efile.save()
            return redirect('EFiles:detail', efile.id)
        else:
            return render(request, 'EFiles/add_efile.html', {'form': form})


def update_efile(request, efile_id):
    if not request.user.is_authenticated:
        return redirect('EFiles:login_user')
    else:
        efile = get_object_or_404(EFile, pk=efile_id)

        if request.method == "POST":
            form = EFileForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                efile.file_name = form.cleaned_data['file_name']
                efile.file_content = form.cleaned_data['file_content']
                efile.save()
                return redirect('EFiles:detail', efile.id)
        else:
            data = {'file_name': efile.file_name, 'file_content': efile.file_content}
            form = EFileForm(initial=data)

        context = {'form': form}
        return render(request, 'EFiles/update_efile.html', context)


class EFileDelete(DeleteView):
    success_url = reverse_lazy('EFiles:index')
    model = EFile


def search(request):
    if not request.user.is_authenticated:
        return redirect('Efiles:login_user')
    else:
        query = request.GET.get("q")
        if query:
            efiles = EFile.objects.all().filter(
                Q(file_name__icontains=query)
            ).distinct()

            return render(request, 'EFiles/index.html',
                          {'user': request.user, 'efiles': efiles})
        else:
            return redirect('EFiles:index')
