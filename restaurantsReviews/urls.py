from django.urls import path, re_path
from . import views

app_name = 'restaurantsReviews'

urlpatterns = [
    re_path('', views.RestaurantList.as_view(), name='restaurant_list'),
    re_path(r'^restaurant/(?P<pk>\d+)/$', views.RestaurantDetial.as_view(), name='restaurant_detial'),
    re_path(r'^restaurant/create/$', views.RestaurantCreate.as_view(), name='restaurant_create'),
    re_path(r'^restaurant/(?P<pk>\d+)/edit/$', views.RestaurantEdit.as_view(), name='restaurant_edit'),
]