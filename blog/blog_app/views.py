from django.shortcuts import render

def index(request):
    context = {
        'title': 'Martyniuk Irina'
    }
    return render(request, 'index.html', context=context)

def blog_detail(request):
    context = {
        'name': 'Martyniuk Irina'
    }
    return render(request, 'blog_datail.html', context=context)