from django.conf.urls import include, url
from django.contrib import admin
from .views import home


urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
