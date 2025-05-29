from django.views.generic import TemplateView
from django.views.generic import View

class HomePageView(TemplateView):
    template_name = 'home_portal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context