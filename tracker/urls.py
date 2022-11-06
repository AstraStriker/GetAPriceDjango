from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('products/<int:myid>', views.product, name="product"),

]