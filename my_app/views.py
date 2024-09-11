from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def category(request):
    return render(request, "categori.html")

def latest_news(request):
    return render(request, "latest_news.html")

def page_blog(request):
    return render(request, "blog.html")

def page_blog_detailes(request):
    return render(request, "blog_details.html")

def blog_elements(request):
    return render(request, "elements.html")

def contact(request):
    return render(request, "contact.html")

