
from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

import admin_notifications
admin_notifications.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view() ,name='index'),
    path('customer/', include('customer.urls')),
    path('store/', include('store.urls')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('checkout/', include('checkout.urls')),
    path('api/', include('rest_framework.urls')),
    path('order/', include('order.urls')),
    path('schedule/', include('schedule.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
