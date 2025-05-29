from django.views.generic import ListView
from games.models.game_category import GameCategory
from games.models.game import Game

class HomePageView(ListView):
    template_name = 'games/home.html'
    context_object_name = 'latest_games'
    queryset = Game.objects.all().order_by('-created_at')[:8]
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GameCategory.objects.all()
        return context