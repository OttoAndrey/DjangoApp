from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):

    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):

    form_model = TagForm
    template = 'blog/tag_create.html'
