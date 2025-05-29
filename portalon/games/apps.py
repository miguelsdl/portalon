from django.apps import AppConfig


class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'games'


# class GamesConfig(AppConfig):
#     name = 'games'
#     verbose_name = _('Games')
#
#     def ready(self):
#         import games.signals  # si tienes señales
#         from . import models  # Importar los modelos