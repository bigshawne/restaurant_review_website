from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField(blank=True, default='')
    phone = models.TextField(blank=True, default='')
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurantsReviews:restaurant_detail', args=[str(self.id)])


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="restaurantsReviews", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurantsReviews:dish_detail', args=[str(self.restaurant.id), str(self.id)])


class Review(models.Model):
    RATING_CHOICE = ((1, 'one'), (2, 'two'), (3, 'Three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=True, default=5, choices=RATING_CHOICE)
    DEFAULT_COMMENT = "The user doesn't leave any comment"
    comment = models.TextField(blank=True, null=True, default=DEFAULT_COMMENT)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="review")

    def __str__(self):
        return "{} review".format(self.restaurant.name)
