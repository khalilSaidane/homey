from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .forms import ListingForm
import accounts.views as account_viwes


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    my_favorites = request.user.profile.favorite_properties.all()
    context = {
        'listings': listings,
        'my_favorites': my_favorites,
    }
    return render(request, 'listings/listings.html', context)


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


def edit_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    form = ListingForm(request.POST or None, request.FILES or None, instance=listing)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts/myproperties')
    else:
        return render(request, 'listings/edit_listing.html', context)


def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.delete()
    return redirect(account_viwes.myproperties)


def like(request, pk):
    '''
    this method add and remove a listing to favorite_properties list
    if the user already likes the listing it will delete it
    if not the listing will be added
    this method can be triggered from the listings page or the myfavorite_properties
    :param request:
    :param pk:
    :return:
    '''
    listing = get_object_or_404(Listing, pk=pk)
    profile = request.user.profile
    if listing in profile.favorite_properties.all():
        profile.favorite_properties.remove(listing)
        profile.save()
        # check the previous page to always redirect to the current page
        if "favorite_properties" in request.META['HTTP_REFERER']:
            return redirect(account_viwes.myfavorite_properties)
        else:
            return redirect('listings')
    else:
        profile.favorite_properties.add(listing)
        profile.save()
        return redirect('listings')
