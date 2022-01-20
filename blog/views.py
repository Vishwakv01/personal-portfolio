from django.shortcuts import render, get_object_or_404
from blog.models import Blogs
# Create your views here.


def bloglist(request):
    blogs_list = Blogs.objects.all()
    return render(request, 'blog/blog_list.html', {'bloglistkey': blogs_list})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_idkey':blogdetail})