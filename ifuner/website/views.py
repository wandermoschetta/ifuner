from django.shortcuts import render


def index(request):
    template_name = 'site.html'
    return render(request, template_name)
