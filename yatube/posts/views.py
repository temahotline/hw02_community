from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_COUNT: int = 10


def index(request):
    posts = Post.objects.select_related('group')[:POSTS_COUNT]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_post.all()[:POSTS_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
