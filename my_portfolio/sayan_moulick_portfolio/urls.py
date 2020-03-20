from django.urls import path
from sayan_moulick_portfolio import test
from .dashboard import getBlogInfo
from . import views
urlpatterns = [
    path('', views.show_myprofile, name='show_myprofile'),
    path('test/', test.hello_world, name='hello_world'),
    path('get-blog-info/', views.getBlogInfo, name='getBlogInfo'),
    path('get-project-detail/<int:pk>/', views.getProjectDetail, name='getProjectDetail'),
    path('fetch-project-detail/', views.fetchProjectDetail, name='fetchProjectDetail')
]
