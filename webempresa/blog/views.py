from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    # diccionario de contexto
    context = {
        'posts': posts,
    }
    return render(request, "blog/blog.html", context)

def category(request, category_id):
    # haciéndolo a mano
    '''
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    '''
    # utilizando consultas inversas de django podemos acceder a category.post_set.all (o el campo 'realted_name' que hayamos definido) en el template category.html
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})