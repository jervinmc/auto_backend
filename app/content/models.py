from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Content(models.Model):
    transmission=models.CharField(_('transmission'),max_length=255,blank=True,null=True)
    brand=models.CharField(_('brand'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    milleage=models.CharField(_('milleage'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    numberOfSeats=models.CharField(_('numberOfSeats'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
