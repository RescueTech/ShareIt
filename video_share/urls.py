from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .views import VideoView

urlpatterns = [
    url(r'^$', login_required(VideoView.as_view()), name='live_stream'),
    url(r'^dvr/$', TemplateView.as_view(template_name="dvr.html"), name='live_stream'),

]
