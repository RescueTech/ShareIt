from django.views.generic.base import TemplateView


class VideoView(TemplateView):

    template_name = "video.html"

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        return context
