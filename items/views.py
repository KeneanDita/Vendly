from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0 )
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items=items.filter(category_id=category_id)
    
    if query:
        items = items.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(created_by__username__icontains=query)
        )
    return render(request, 'items/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[:4]
    
    return render(request, 'items/detail.html', {'item': item, 'related_items': related_items})

def category_items(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = Item.objects.filter(category=category, is_sold=False)
    return render(request, 'items/category_items.html', {
        'category': category,
        'items': items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'Edit Item',
    })