from django.shortcuts import render, get_object_or_404
from .models import Postt
# Create your views here.
def home(request):
    posts = Postt.objects.order_by('-publish_date')
    return render(request, 'post/home.html', {'posts':posts})

def post_details(request, post_id):
    post = get_object_or_404(Postt, pk=post_id)
    return render(request, 'post/post_detail.html', {'post': post})
