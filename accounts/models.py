from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(_('Profile Image'),
                               upload_to='users/%Y/%m/%d', blank=True)
    full_name = models.CharField(
        _('Full name'), max_length=100, null=True, blank=True, default="")

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('email',)
