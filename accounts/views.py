from django.shortcuts import render

def trial(request):
    return render(request, 'accounts/profiles.html')
