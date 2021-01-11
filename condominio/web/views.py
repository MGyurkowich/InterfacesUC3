from django.shortcuts import render


def home(request):

    return render(request, 'web/home.html')


def profile(request):
    return render(request, 'web/profile.html')


def messages(request):
    return render(request, 'web/messages.html')


def bills(request):
    return render(request, 'web/bills.html')


def payments(request):
    return render(request, 'web/payment.html')


def calendar(request):
    return render(request, 'web/calender.html')


def ajustes(request):
    return render(request, 'web/settings.html')

