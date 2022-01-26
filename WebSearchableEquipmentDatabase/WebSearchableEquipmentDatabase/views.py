from django.shortcuts import render, redirect

def landing(request):
    context = {'home': True,
               }
    return render(request, 'landing.html', context)
