from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CommentForm

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})
