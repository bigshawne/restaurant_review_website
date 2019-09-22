from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .forms import RestaurantForm

from restaurantsReviews.models import Restaurant, RestaruantReview, Dish


class RestaurantList(ListView):
    queryset = Restaurant.objects.all().order_by('-date')
    context_object_name = 'latest_restaurant_list'
    tempalte_name = 'restaurantsReviews/restaurant_list.html'


class RestaurantDetial(DetailView):
    model = Restaurant
    template_name = 'restaurantsReviews/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetial, self).get_context_data(**kwargs)
        context['RATING_CHOICE'] = RestaruantReview.RATING_CHOICE
        return context


class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = template_name = 'restaurantsReviews/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class RestaurantEdit(UpdateView):
    model = Restaurant
    template_name = 'restaurantsReviews/form.html'
    form_class = RestaurantForm
