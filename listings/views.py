from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html',context)


def new_listing(request):
    form = ListingForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listings')
    else:
        return render(request, 'listings/new_listing.html', context)
