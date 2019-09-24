from django.urls import path, re_path
from . import views

app_name = 'restaurantsReviews'

urlpatterns = [
    # Check all restaurants
    path('', views.RestaurantList.as_view(), name='restaurant_list'),
    # Check the detail of selected restaurant
    re_path(r'^restaurant/(?P<pk>\d+)/$', views.RestaurantDetail.as_view(), name='restaurant_detail'),
    # Create restaurant
    re_path(r'^restaurant/create/$', views.RestaurantCreate.as_view(), name='restaurant_create'),
    # Edit restaurant
    re_path(r'^restaurant/(?P<pk>\d+)/edit/$', views.RestaurantEdit.as_view(), name='restaurant_edit'),
    # Create dish
    re_path(r'^restaurant/(?P<pk>\d+)/dishes/create/$', views.DishCreate.as_view(), name='dish_create'),
    # Edit dish
    re_path(r'^restaurant/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$', views.DishEdit.as_view(), name='dish_edit'),
    # Details of dish
    re_path(r'^restaurant/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$', views.DishDetail.as_view(), name='dish_detail'),
    # Create reviews
    re_path(r'^restaurant/(?P<pk>\d+)/reviews/create/$', views.review_create, name='review_create'),
]
