from django.conf.urls import url
from .views import VideoView

urlpatterns = [
    url(r'', VideoView.as_view(), name='live_stream'),

]
