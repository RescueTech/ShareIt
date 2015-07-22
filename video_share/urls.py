from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .views import VideoView

urlpatterns = [
    url(r'^$', login_required(VideoView.as_view()), name='live_stream'),
    url(r'^dvr/$', login_required(TemplateView.as_view(template_name="dvr.html")), name='dvr_stream'),

]
