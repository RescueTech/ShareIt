from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import VideoView

urlpatterns = [
    url(r'^$', login_required(VideoView.as_view()), name='live_stream'),

]
