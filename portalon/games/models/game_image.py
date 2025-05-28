from django.db import models
from django.utils.translation import gettext_lazy as _
from game import Game
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class GameImage(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = FilerImageField(
        verbose_name=_('image'),
        on_delete=models.CASCADE
    )
    name = models.CharField(_('name'), max_length=100, blank=True)
    description = models.TextField(_('description'), blank=True)
    order = models.PositiveIntegerField(
        _('order'),
        default=0,
        help_text=_('Display order of the image')
    )

    class Meta:
        verbose_name = _('game image')
        verbose_name_plural = _('game images')
        ordering = ['order']

    def __str__(self):
        return f"{self.game.title} - {self.name}"