from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import price_choices, category_choices
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, UpdateForm

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings  = paginator.get_page(page)
    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    context = {
        'listing': listing
    }
    return render(request,'listings/listing.html', context)

def search(request):
    query_set= Listing.objects.order_by('list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    if 'category' in request.GET:
        keywords = request.GET['category']
        if keywords:
            query_set = query_set.filter(description__iexact=category_choices)
    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            query_set = query_set.filter(description__iexact=price_choices)
    context ={
      'query_set': query_set,
      'category_choices': category_choices,
     'price_choices': price_choices,
     'values': request.GET
           }
    return render(request, 'listings/search.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            return redirect('dashboard')
        else:
            pass
    else:
        return render(request,'listings/create.html',{'form': ListingForm()})


@login_required
def update(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    context = {
        'form': UpdateForm(instance=listing),
        'update': True,
        'pk': pk
    }
    if request.method=="POST":
        form = UpdateForm(request.POST,request.FILES,instance=listing)
        print(form)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        return render(request, 'listings/create.html', context)

@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method=="POST":
        listing.delete()
        return redirect('dashboard')
