from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

# Home page: show all items


def home(request):
    items = Item.objects.all().order_by('-date')
    return render(request, 'home.html', {'items': items})

# Add a new lost/found item


def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        location = request.POST['location']
        contact = request.POST['contact']
        status = request.POST['status']

        Item.objects.create(
            name=name,
            description=desc,
            location=location,
            contact=contact,
            status=status,
        )
        return redirect('home')
    return render(request, 'add_item.html')

# Mark an item as claimed


def mark_claimed(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.status = 'claimed'
    item.save()
    return redirect('home')
