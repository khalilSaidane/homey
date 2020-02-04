from django.urls import path

from . import views

urlpatterns = [
    path('/', views.listings, name='listings'),
    path('/add', views.new_listing, name='new_listing'),
    path('/edit/<int:pk>', views.edit_listing, name='edit_listing'),
    path('/delete/<int:pk>', views.delete_listing, name='delete_listing'),
    path('/like/<int:pk>', views.like, name='like'),
    path('/myproperties', views.myproperties, name='myproperties'),
    path('/favorite_properties', views.myfavorite_properties, name='favorite_properties'),
]
