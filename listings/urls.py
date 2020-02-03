from django.urls import path

from . import views

urlpatterns = [
    path('/', views.listings, name='listings'),
    path('/add', views.new_listing, name='new_listing'),
    path('/edit/<int:pk>', views.edit_listing, name='edit_listing'),
    path('/delete/<int:pk>', views.delete_listing, name='delete_listing'),
    path('/like/<int:pk>', views.like, name='like'),
]
