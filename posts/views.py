from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Post, Comment
from .form import PostForm

def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {'posts':my_list}
    return render(request,'list.html', context)

def p_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form':post_form})

def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:list')

def p_edit(request, post_id):
    post = get_object_or_404(Post, pk = post_id)

    if request.method == "POST":
        post_form = PostForm(request.POST,instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        post_form = PostForm(instance=post)

    return render(request, 'create.html', {'post_form':post_form})

def p_detail(request, post_id):
    detail = Post.objects.get(pk = post_id)
    comment = Comment.objects.get(post=post_id)

    return render(request, 'detail.html', {'detail': detail, 'comment': comment})

