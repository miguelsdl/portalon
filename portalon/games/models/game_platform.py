from django.db import models
from django.utils.translation import gettext_lazy as _


class GamePlatform(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('platform')
        verbose_name_plural = _('platforms')

    def __str__(self):
        return self.name
