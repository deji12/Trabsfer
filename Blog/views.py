from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

def Home(request):

    get_blogs = Post.objects.filter(published=True).order_by('-date')

    p = Paginator(get_blogs, 10)
    page = request.GET.get('page')
    page_series = p.get_page(page)

    context = {
        'pages': page_series,
    }

    return render(request, "blog-grid.html", context)

def PostDetail(request, slug):

    get_post_by_slug = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(published=True).exclude(slug=get_post_by_slug.slug)[:4]

    if request.method == 'POST':
        name = request.POST.get('name')
        email  = request.POST.get('email')
        website = request.POST.get('website')
        comment = request.POST.get('comment')

        new_comment = Comment(post=get_post_by_slug, name=name, email=email, content = comment)
        if website:
            new_comment.website = website
        new_comment.save()

        get_post_by_slug.number_of_comments += 1
        get_post_by_slug.save()

        return redirect('post-detail', slug=slug)

    context = {
        "post": get_post_by_slug,
        "related": related_posts,
    }

    return render(request, "blog-single.html", context)