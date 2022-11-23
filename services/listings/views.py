from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Comment
from django.core.paginator import Paginator, EmptyPage
from .choices import price_choices, CATEGORY_CHOICES
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, UpdateForm, CommentForm
from django.views.generic import CreateView

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
    rate = False
    favourite = False
    listing = get_object_or_404(Listing, pk=pk)
    if request.user.is_authenticated:

        favourites = str(request.user.favourites)
        favourites = favourites.split(',')

        rate_listing = str(request.user.rate_listing)
        rate_listing = rate_listing.split(',')
        if request.method== "POST":
            if 'favourite_val' in request.POST:
                favourite_val = request.POST['favourite_val']
                if favourite_val == 'unfavourite':
                    if str(pk) in favourites:
                        favourites.remove(str(pk))
                if favourite_val == 'favourite':
                    if str(pk) not in favourites:
                        favourites.append(str(pk))
                request.user.favourites = ','.join(favourites)
                request.user.save()

            if 'my_rating' in request.POST:
                my_rating = request.POST['my_rating']
                if int(my_rating)>10 or int(my_rating) <0:
                    messages.error(request,'Ingresar un valor de 0 a 10')
                elif (str(pk)) not in rate_listing:
                    if listing.total_rating:
                        listing.total_rating += int(request.POST['my_rating'])
                        listing.no_of_rating += 1
                    else:
                        listing.total_rating = int(request.POST['my_rating'])
                        listing.no_of_rating = 1
                    rate_listing.append (str(pk))
                    request.user.rate_listing = ','.join(rate_listing)
                    request.user.save()
                    listing.save()

        if str(pk) in favourites:
            favourite = True
        if str(pk) not in rate_listing:
            rate = True

    current_rating = 0
    tRating = listing.no_of_rating
    if listing.no_of_rating:
        current_rating = listing.total_rating/listing.no_of_rating
    context = {
        'listing': listing,
        'favourite': favourite,
        'rate': rate,
        'current_rating': current_rating,
        'tRating': tRating
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
            query_set = query_set.filter(description__iexact=CATEGORY_CHOICES[int(keywords)][1])
    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            query_set = query_set.filter(description__iexact=price_choices)
    context ={
      'query_set': query_set,
      'category_choices': CATEGORY_CHOICES,
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
            return render(request, 'listings/create.html', {'form': form})
            
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

@login_required
def comments(request,pk):
    listing = get_object_or_404(Listing,pk=pk)
    #listing = Comment.objects.all(pk=pk)
    context = {
        'form': CommentForm(instance=listing),
        'pk':pk
    }
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=listing)
        #form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listings')
        else:
            #return render(request,'listings/comment.html',context)
            return Comment.objects.filter(body=listing).all()

""""
@login_required
def comments(request,pk):
    listing = get_object_or_404(Comment,pk=pk)
    context = {
        'form': CommentForm(instance=listing),
        'pk':pk
    }
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=listing)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listings')
        else:
            return render(request,'listings/comment.html',context)
"""