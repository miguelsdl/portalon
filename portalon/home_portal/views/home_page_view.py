from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home_portal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Aquí puedes agregar datos adicionales para la página
        return context