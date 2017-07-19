from django.shortcuts import render


# Create your views here.


def hello(request):
    return render(request, 'app01_html/hello.html')
