from django.shortcuts import render, redirect
from items.models import Item, Category
from .forms import SignupForm
from django.contrib.auth import logout as auth_logout


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories,
    })


def contact(request):
    return render(request, "core/contact.html")

def about(request):
    return render(request, "core/about.html")

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")
def terms_of_use(request):
    return render(request, "core/terms_of_use.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {"form": form})

def logout(request):
    auth_logout(request)
    return redirect('/')

