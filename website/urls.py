from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('contact',views.contact,name='contact'),
   path('about',views.about,name='about'),
   path('service',views.service,name='service'),
   path('pricing',views.pricing,name='pricing'),
   path('blog',views.blog,name='blog'),
   path('blog_detail',views.blog_detail,name='blog_detail'),
]
