from django.shortcuts import render
from django.shortcuts import redirect
from django.urls.base import reverse


# Create your views here.
def main(request):
    return render(request, 'article/base.html', {})


def rus(request):
    return render(request, 'article/rus.html', {})


def eng(request):
    return render(request, 'article/eng.html', {})


def rus1(request):
    return render(request, 'article/1_r.html', {})


def rus2(request):
    return render(request, 'article/2_r.html', {})


def rus3(request):
    return render(request, 'article/3_r.html', {})


def rus4(request):
    return render(request, 'article/4_r.html', {})


def rus5(request):
    return render(request, 'article/5_r.html', {})


def eng1(request):
    return render(request, 'article/1_e.html', {})


def eng2(request):
    return render(request, 'article/2_e.html', {})


def eng3(request):
    return render(request, 'article/3_e.html', {})


def eng4(request):
    return render(request, 'article/4_e.html', {})


def eng5(request):
    return render(request, 'article/5_e.html', {})
