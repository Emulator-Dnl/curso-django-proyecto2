from django.shortcuts import render, HttpResponse

# Create your views here.
# En core dejaremos solamente las páginas estáticas, en éste caso home, about, store
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")