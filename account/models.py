from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    is_active = models.BooleanField(verbose_name="Active", default=True)
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False, verbose_name=_('Admin'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))

    first_name = None
    last_name = None

    def save(self, *args, **kwargs):
        try:
            if kwargs['password']:
                self.set_password(kwargs['password'])
        except Exception:
            pass
        finally:
            super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'account'
        verbose_name = _("User")
        verbose_name_plural = _("Users")