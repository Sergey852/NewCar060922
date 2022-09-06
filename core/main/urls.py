from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('about/about_details/<str:id>', views.AboutdetailListView.as_view(), name='about_details'),
    path('about/about_details2/<str:id>', views.Aboutdetail2ListView.as_view(), name='about_details2'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('gallery/Gallery_view_more/<int:id>', views.GalleryphotoDetailView.as_view(), name='Gallery_view_more'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/<str:id>', views.CarCategListView.as_view(), name='car_categ'),
    path('services/', views.ServicesListView.as_view(), name='services'),
    

]