from django.db import models
from django.utils.translation import gettext_lazy as _


class Items(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    imageUrl = models.FileField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Item')
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
