from django.shortcuts import render, redirect
from category.forms import CategoryForm

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('add_category')
    else:
        cat_form = CategoryForm()
    return render(request, 'add_category.html', {'form': cat_form})