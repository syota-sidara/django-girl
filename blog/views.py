from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.


def post_list(request):
    contents = {
        # オブジェクトのデータ全部を取得しそれをコンテンツに入れる
        # 作成順に並べるには.order_by()と作成時のデータを持ってくる
        'posts': Post.objects.all().order_by('-created_data')
    }
    return render(request, 'blog/post_list.html', contents)

# requestは色々な情報が入っているもの


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_data = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
