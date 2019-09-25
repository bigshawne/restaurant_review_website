import json
from django.db.models import Q
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .forms import RestaurantForm, DishForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Restaurant, RestaurantReview, Dish


class RestaurantList(ListView):
    queryset = Restaurant.objects.all().order_by('-date')
    context_object_name = 'latest_restaurant_list'
    template_name = 'restaurantsReviews/restaurant_list.html'


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'restaurantsReviews/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICE'] = RestaurantReview.RATING_CHOICE
        return context


class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'restaurantsReviews/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class RestaurantEdit(UpdateView):
    model = Restaurant
    template_name = 'restaurantsReviews/form.html'
    form_class = RestaurantForm


class DishDetail(DetailView):
    model = Dish
    template_name = 'restaurantsReviews/dish_detail.html'


class DishCreate(CreateView):
    model = Dish
    template_name = 'restaurantsReviews/form.html'
    form_class = DishForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_invalid(form)


class DishEdit(UpdateView):
    model = Dish
    template_name = 'restaurantsReviews/form.html'
    form_class = DishForm


def review_create(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['review'],
        user=request.user,
        restaurant=restaurant
    )

    review.save()
    return HttpResponseRedirect(reverse('restaurantsReviews:restaurant_detail', args=[pk]))


def restaurant_search(request):
    q = request.GET.get('q', None)
    if q:
        queryset = Restaurant.objects.filter(Q(name__contains=q))
        context = {'latest_restaurant_list': queryset}
        return render(request, 'restaurantsReviews/restaurant_search.html', context=context)
    return render(request, 'restaurantsReviews/restaurant_search.html')


def restaurant_ajax_research(request):
    q = request.GET.get('q', None)
    if q:
        restaurant_list = Restaurant.objects.filter(Q(name__contains=q))
        data = []
        for restaurant in restaurant_list:
            data.append({"name": restaurant.name})
        json_data = json.dumps(data)
        return HttpResponse(json_data)

