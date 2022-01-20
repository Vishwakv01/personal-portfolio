from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.bloglist, name='bloglist'),
    path('<int:blog_id>', views.detail, name='blogdetail'),
]