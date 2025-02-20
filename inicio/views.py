from django.shortcuts import render, redirect
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm, BuscarPostForm

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'inicio/lista_posts.html', {'posts': posts})

def ver_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comentarios = Comentario.objects.filter(post=post)
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
            return redirect('ver_post', post_id=post.id)
    else:
        comentario_form = ComentarioForm()
    return render(request, 'inicio/ver_post.html', {'post': post, 'comentarios': comentarios, 'comentario_form': comentario_form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'inicio/crear_post.html', {'form': form})

def buscar_posts(request):
    form = BuscarPostForm(request.GET)
    posts = Post.objects.all()
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        if busqueda:
            posts = posts.filter(titulo__icontains=busqueda)
    return render(request, 'inicio/buscar_posts.html', {'form': form, 'posts': posts})
