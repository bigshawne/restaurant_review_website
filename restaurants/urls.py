from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('accounts/', include('allauth.urls')),
    url('accounts/', include('myaccount.urls')),
    url('restaurantsReviews/', include('restaurantsReviews.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
