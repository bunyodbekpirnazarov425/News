"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import home, about, blog_elements, page_blog_detailes, page_blog, category,contact, latest_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('about/', about, name="about_page"),
    path('elements/', blog_elements, name="elements_page"),
    path('blog_details/', page_blog_detailes, name="details_page"),
    path('blog/', page_blog, name="blog_page"),
    path('category/', category, name="category_page"),
    path('contact/', contact, name="contact_page"),
    path('latest_news/', latest_news, name="latest_news_page"),
]

