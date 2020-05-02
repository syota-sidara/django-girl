from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    contents = {
        # オブジェクトのデータ全部を取得しそれをコンテンツに入れる
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', contents)


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
