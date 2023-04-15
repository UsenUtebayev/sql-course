from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='index.html', context={"title": "SQL курсының сайтына қош келдіңіз!"})


def about(request):
    return render(request, template_name='about.html', context={"title": "Біз туралы"})


def doc(request):
    return render(request, template_name='doc1.html', context={"title": "Курс"})
